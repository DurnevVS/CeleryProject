from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.main.models import AbstractModel


class Message(AbstractModel):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    body = models.TextField(verbose_name=_('Тело сообщения'))
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Сообщение')
        verbose_name_plural = _('Сообщения')
