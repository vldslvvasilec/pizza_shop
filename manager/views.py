from django.shortcuts import render
from pizza_main_app.models import Menu

# Create your views here.

def manager(request):
    page_title = 'Manager consol'
    drop_menu = Menu.objects.all()
    return render(request, 'base_manager.html', {'drop_items': drop_menu, 'global_title': page_title})
