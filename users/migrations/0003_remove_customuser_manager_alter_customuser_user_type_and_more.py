# Generated by Django 5.0.3 on 2024-04-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='manager',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('buyer', 'Buyer'), ('manager', 'Manager'), ('chef', 'Chef')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
