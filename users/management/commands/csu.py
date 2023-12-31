from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='usachev@mail.ru',
            first_name='Oleg',
            last_name='Usachev',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('alexia1456')
        user.save()

