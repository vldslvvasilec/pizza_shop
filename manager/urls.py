from django.urls import path
from .views import manager, all_products, manage_pizza, manage_sushi, manage_sets, manage_buyers, manage_chefs, manage_managers, test

app_name = 'manager'

urlpatterns = [
    path('manager/', manager, name='manager_main'),

    path('manager/all_product/', all_products, name='all_products'),

    path('manager/Pizza_manage/', manage_pizza, name='manage_pizza'),
    path('manager/Sushi_manage', manage_sushi, name='manage_sushi'),
    path('manager/Sets_manage/', manage_sets, name='manage_setss'),

    path('manager/buyers/', manage_buyers, name='buyers'),
    path('manager/chefs/', manage_chefs, name='chefs'),
    path('manager/managers/', manage_managers, name='managers'),

    path('test', test, name='test')
]