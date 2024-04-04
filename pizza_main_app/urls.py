from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from pizza_main_app import views

urlpatterns = [
    path('Pizza/', views.pizza, name='Pizza'),
    path('Sushi/', views.sushi, name='Sushi'),
    path('Sets/', views.sets, name='Sets'),
    path('All_menu/', views.home, name='all_menu'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
