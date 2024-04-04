from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pizza_main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='all_menu'),
    path('', include('pizza_main_app.urls')),
    path('', include('users.urls')),
    path('', include('manager.urls')),
    path('', include('cook.urls')),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
