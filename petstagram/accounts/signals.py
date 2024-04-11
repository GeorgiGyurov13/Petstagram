from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from petstagram import settings
from petstagram.accounts.models import Profile

UserModel = get_user_model


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def send_email_when_register_user(user):
    html_message = render_to_string(
        'accounts/welcome_email.html',
        {'user': user}
    )
    plain_message = strip_tags(html_message)
    send_mail(
        subject="Registration successfully",
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=('georgigyurov387@gmail.com',),
    )


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_email_when_register_user(instance)
