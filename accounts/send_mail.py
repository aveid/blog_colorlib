from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_message_to_email(email, activation_code):
    context = {
        "email": email,
        "domain": " http://127.0.0.1:8000",
        "activation_code": activation_code
    }
    message = render_to_string("email.html", context)
    finaly_message = strip_tags(message)
    send_mail(
        'Активация аккаунта',
        finaly_message,
        settings.EMAIL_HOST_USER,
        [email, ],
        html_message=message,
    )
