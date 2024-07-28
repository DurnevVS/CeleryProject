from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.main.models import AbstractModel


class Task(AbstractModel):
    messege = models.ForeignKey('clients.Message', on_delete=models.CASCADE, verbose_name=_('Сообщение'))
    task = models.OneToOneField(
        'django_celery_beat.PeriodicTask', 
        on_delete=models.CASCADE, 
        verbose_name=_('Задача'),
        related_name='client_task'
        )

    def __str__(self) -> str:
        return self.task.name

    class Meta:
        verbose_name = _('Рассылка')
        verbose_name_plural = _('Рассылка')
