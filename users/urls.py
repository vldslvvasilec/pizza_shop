from django.urls import path
from .views import SignUpView, LoginView, MainView, logout_view

urlpatterns = [
    path('registr/', SignUpView.as_view(), name='registr'),
    path('login/', LoginView.as_view(), name='login'),
    path('main/', MainView.as_view(), name='main'),
    path('logout/', logout_view, name='logout'),
]
