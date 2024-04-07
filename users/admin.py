from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAndManagerAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')
    list_filter = ('user_type',)  # Добавьте запятую, чтобы указать кортеж
    search_fields = ('username', 'email', 'first_name', 'last_name')

    def manager_first_name(self, obj):
        return obj.manager.first_name if obj.manager else ''

    def manager_last_name(self, obj):
        return obj.manager.last_name if obj.manager else ''

admin.site.register(CustomUser, CustomUserAndManagerAdmin)
