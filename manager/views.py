from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from pizza_main_app.models import Menu


def manager(request):
    page_title = 'Manager consol'
    drop_menu = Menu.objects.all()
    return render(request, 'main_manage.html', {'drop_items': drop_menu, 'global_title': page_title})

def all_products(request):
    page_title = 'Produktový management'
    drop_menu = Menu.objects.all()
    content = 'all products'
    return render(request, 'main_manage.html', {'drop_items': drop_menu, 'global_title': page_title, 'main_content': content})

def manage_pizza(request):
    page_title = 'Změny Pizza'
    drop_menu = Menu.objects.all()
    content = 'Změny Pizza'
    return render(request, 'main_manage.html', {'drop_items': drop_menu, 'global_title': page_title, 'main_content': content})

def manage_sushi(request):
    page_title = 'Změny Sushi'
    drop_menu = Menu.objects.all()
    content = 'Změny Sushi'
    return render(request, 'main_manage.html', {'drop_items': drop_menu, 'global_title': page_title, 'main_content': content})

def manage_sets(request):
    page_title = 'Změny Sets'
    drop_menu = Menu.objects.all()
    content = 'Změny Sets'
    return render(request, 'main_manage.html', {'drop_items': drop_menu, 'global_title': page_title, 'main_content': content})

def manage_buyers(request):
    page_title = 'Naši yákazíci'
    drop_menu = Menu.objects.all()
    content = 'Naši zákazíci'
    return render(request, 'main_manage.html', {'drop_items': drop_menu, 'global_title': page_title, 'main_content': content})

def manage_chefs(request):
    page_title = 'Naši kuchaři'
    drop_menu = Menu.objects.all()
    content = 'Naši kuchaři'
    return render(request, 'main_manage.html', {'drop_items': drop_menu, 'global_title': page_title, 'main_content': content})

def manage_managers(request):
    page_title = 'Naši manažeři'
    drop_menu = Menu.objects.all()
    content = 'Naši manažeři'
    return render(request, 'main_manage.html', {'drop_items': drop_menu, 'global_title': page_title, 'main_content': content})

class LoginManagerView(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'registration/template_login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        status = 'valid'
        return super().form_valid(form)

    def form_invalid(self, form):
        status = 'invalid'
        return redirect(reverse('registr'))
    
def logout_view(request):
    logout(request)
    return redirect('/')

def test(request):
    return render(request, 'loging_manage.html')
