from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('generate/', include('image_gen.urls')),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$',serve,{'document.root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
]
