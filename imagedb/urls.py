"""imagedb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from imagedb.images.views import ImageCreateView, ImageListView, ImageDetailView, ImageDownloadView

urlpatterns = [
    path('', ImageListView.as_view(), name='index'),
    path('image/upload/', ImageCreateView.as_view(), name='image-create'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('image/<int:pk>/download/', ImageDownloadView.as_view(), name='image-download'),
    path('images/', ImageListView.as_view(), name='image-list'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
