from core import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
