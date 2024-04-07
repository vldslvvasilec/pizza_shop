from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# class Manager(models.Model):
#     user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='manager_profile')
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('buyer', 'Buyer'),
        ('manager', 'Manager'),
        ('chef', 'Chef'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchase_history = models.TextField(blank=True)

    # # Указываем имена обратных отношений для связей с группами и правами пользователей
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username


