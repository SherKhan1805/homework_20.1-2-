# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from django.utils.crypto import get_random_string
# from django.contrib.auth import get_user_model
# from users.models import EmailVerification
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
#
# User = get_user_model()
#
#
# @receiver(pre_save, sender=User)
# def create_email_verification(sender, instance, **kwargs):
#     if not hasattr(instance, '_dirty'):
#         instance._dirty = True
#         email_verification, created = EmailVerification.objects.get_or_create(user=instance)
#         if created or not email_verification.token:
#             email_verification.token = get_random_string(32)
#             email_verification.is_verified = False
#             email_verification.save()
#         instance._dirty = False
#
#
# @receiver(post_save, sender=User)
# def send_verification_email(sender, instance, created, **kwargs):
#     if created and not instance.emailverification.is_verified:
#         # Генерация и отправка электронного письма
#         subject = 'Подтверждение электронной почты'
#         message = render_to_string('email/verification_email.txt', {'user': instance})
#         from_email = 'usaechv97@mail.ru'
#         to_email = instance.email
#
#         send_mail(subject, message, from_email, [to_email])
