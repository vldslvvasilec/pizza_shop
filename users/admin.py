from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Manager

class CustomUserAndManagerAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'manager_first_name', 'manager_last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'manager__first_name', 'manager__last_name')

    def manager_first_name(self, obj):
        return obj.manager.first_name if obj.manager else ''

    def manager_last_name(self, obj):
        return obj.manager.last_name if obj.manager else ''

admin.site.register(CustomUser, CustomUserAndManagerAdmin)
admin.site.register(Manager)
