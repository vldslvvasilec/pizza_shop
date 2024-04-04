from django.urls import path
from .views import manager

urlpatterns = [
    path('manager/', manager, name='manager_main'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('main/', MainView.as_view(), name='main'),
    # path('logout/', logout_view, name='logout'),
]