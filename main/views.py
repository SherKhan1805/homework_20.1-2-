from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Product, Contact, Version
from main.forms import ProductForm, VersionFormSet

from django.db.models import OuterRef, Subquery
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from main.services import get_categories_from_cache


# Create your views here.


class ProductListView(LoginRequiredMixin, ListView):
    """
    Класс для создания списка продуктов
    """
    model = Product
    template_name = 'main/index.html'

    def get_queryset(self):
        """
        Возвращает активную версию продукта для отображения в карточке продукта
        """
        return Product.objects.annotate(
            active_version_number=Subquery(
                Version.objects.filter(
                    product=OuterRef('pk'),
                    is_active_version=True,
                ).values('number_version')[:1]
            )
        )


def contacts(request):
    """
    Функция получает данные, введенные пользователем
    """

    contacts_ = Contact.objects.all()
    return render(request, 'main/contacts.html', {'contacts': contacts_})


def categories(request):
    """
    Вывод списка категорий продуктов с использованием низкоуровневого кэширования
    """
    categories_list = get_categories_from_cache()
    return render(request, 'main/categories.html', {'categories_list': categories_list})


# @cache_page(60)
class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Класс для выведения информации о продукте
    """
    model = Product
    template_name = 'main/product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для создания продукта
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:index')
    template_name = 'main/new_product_form.html'

    def __init__(self):
        self.request = None
        self.object = None

    def get_context_data(self, **kwargs):
        """
        Получаем список версий продукта из формсета
        """
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['version_formset'] = VersionFormSet(self.request.POST)
        else:
            data['version_formset'] = VersionFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        version_formset = context['version_formset']
        if version_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.author = self.request.user  # Установка автора продукта
            self.object.save()
            version_formset.instance = self.object
            version_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Класс для обновления данных о продукте
    """
    model = Product
    fields = ('name', 'description', 'image', 'category')
    permission_required = 'main.edit_published'
    success_url = reverse_lazy('main:index')
    template_name = 'main/product_update.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None
        self.request = None

    def test_func(self):
        """
        Проверка, является ли текущий пользователь автором или модератором продукта
        """
        user = self.request.user
        product_author = self.get_object().author
        return user == product_author or user.groups.filter(name="moderator").exists()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['version_formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            data['version_formset'] = VersionFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        """
        Метод для установки версии продукта
        """
        context = self.get_context_data()
        version_formset = context['version_formset']

        if version_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.author = self.request.user
            version_formset.instance = self.object
            version_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form(self, form_class=None):
        """
        Переопределение метода чтобы динамически изменять поля формы
        в зависимости от принадлежности пользователя к группе "moderator".
        Если пользователь является модератором, поля 'name' и 'image' удаляются из формы.
        """
        form = super().get_form(form_class)
        user = self.request.user

        if user.groups.filter(name="moderator").exists():
            form.fields.pop('name')
            form.fields.pop('image')

        return form


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')
    template_name = 'main/product_confirm_delete.html'

    def test_func(self):
        """
        Проверка, является ли текущий пользователь автором продукта
        """
        return self.request.user == self.get_object().author


def custom_permission_denied(request, exception):
    """
    При ошибке изменения или удаления товара перевод на собственную страницу
    """
    return render(request, 'main/403.html', status=403)


def toggle_publish(request, pk):
    """
    Функция проверяет статус публикации и присваивает противоположное значение
    """
    product_item = get_object_or_404(Product, pk=pk)

    # Проверка на наличие пермиссий у пользователя для публикации/снятия
    # с публикации продукта
    # Если прав нет идет обработка ошибки 403
    if request.user.has_perm('catalog.edit_published'):
        product_item.is_published = not product_item.is_published
        product_item.save()
        return redirect(reverse('main:index'))
    else:
        # Обработка случая, когда у пользователя нет нужных прав
        return render(request, 'main/403.html')
