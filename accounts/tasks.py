from accounts.send_mail import send_message_to_email
from main.celery import app


@app.task
def send_message(email, activation_code):
    send_message_to_email(email, activation_code)
    return "success"
