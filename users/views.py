from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect, render

class SignUpView(FormView):
    template_name = 'registr.html'  # Путь к шаблону для страницы регистрации
    form_class = CustomUserCreationForm
    success_url = '/'  # Перенаправление после успешной регистрации

    def form_valid(self, form):
        # Сохраняем пользователя
        user = form.save()

        # Аутентификация пользователя
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)

        # Входим в систему после успешной регистрации
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['global_title'] = 'Registrace'
        return context


class LoginView(FormView):
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


class MainView(TemplateView):
    template_name = 'main.html'


def logout_view(request):
    logout(request)
    return redirect('/')
