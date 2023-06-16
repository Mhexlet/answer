from django.contrib import admin

# Register your models here.
from .models import Objections

class ObjectionsAdmin(admin.ModelAdmin):
    list_display = ['textObjections', 'answer']

admin.site.register(Objections, ObjectionsAdmin )