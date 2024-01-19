from celery import shared_task
from django.core.mail import send_mail


# Определяем Celery задачу для отправки электронной почты
@shared_task
def send_allauth_email(subject, message, from_email, recipient_list):
    # Используем функцию send_mail из django.core.mail для отправки электронной почты
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
    )
