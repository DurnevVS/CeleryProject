from django.shortcuts import render

# Create your views here.

from django_celery_beat.models import PeriodicTask

def start_task(request):
    task = PeriodicTask.objects.get(id=7)
