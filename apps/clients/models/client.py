from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.main.models import AbstractModel


class Client(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    name = models.CharField(max_length=255, verbose_name=_('Имя'))
    email = models.EmailField(verbose_name=_('email'))
    comment = models.TextField(verbose_name=_('Комментарий'), blank=True, null=True)
    tasks = models.ManyToManyField('clients.Task', verbose_name=_('Рассылки'), blank=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')
