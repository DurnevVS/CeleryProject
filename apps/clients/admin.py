from django.contrib import admin
from .models import Client, Message, Task

admin.site.register((Client, Message, Task))
