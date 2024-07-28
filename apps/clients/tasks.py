from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Client, Message


@shared_task(name=_('Рассылка писем'))
def send_email_task(): #from_user_id: int, to_client_id: int, message_id: int) -> int:
    print('start task')
    # user = get_user_model().objects.get(id=from_user_id)
    # client = Client.objects.get(id=to_client_id)
    # message = Message.objects.get(id=message_id)

    # response_code = send_mail(
    #     subject=message.title,
    #     message=message.body,
    #     from_email=user.email,
    #     recipient_list=[client.email],
    #     fail_silently=False
    # )
    
    # return response_code
