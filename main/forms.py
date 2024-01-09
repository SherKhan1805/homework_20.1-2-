from django import forms

from main.models import Product, Version
from django.forms import inlineformset_factory, BaseInlineFormSet

words_unused = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    """
    Форма для валидации и стилизации продукта
    """

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'category1', 'image', 'price', 'create_date', 'edit_date']
        widgets = {
            'author': forms.HiddenInput(),
        }

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        if cleaned_name in words_unused:
            raise forms.ValidationError('Продукт запрещен к продаже на нашем сайте')

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        if cleaned_description in words_unused:
            raise forms.ValidationError('Описание продукта недопустимо на нашем сайте')

        return cleaned_description

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    """
    Форма для версии продукта
    """

    class Meta:
        model = Version
        fields = '__all__'


# Формсет для выведения выбора версии и ее активности при создании и обновлении продукта
VersionFormSet = inlineformset_factory(Product, Version, fields=['number_version', 'is_active_version'], extra=1)