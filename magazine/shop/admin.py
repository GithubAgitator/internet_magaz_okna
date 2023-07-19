from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name'] # какие поля будем показывать
    # list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name',] # по какому полю сортируем
    # fields = ['email']
    search_fields = ['name'] # поле где можно вбивать поиск по имени

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)

