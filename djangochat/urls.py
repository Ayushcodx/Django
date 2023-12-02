from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('generate/', include('image_gen.urls')),
    path('admin/', admin.site.urls),
]
