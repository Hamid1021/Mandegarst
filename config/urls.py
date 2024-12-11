"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls', namespace="account")),
    path('', include('application.urls', namespace="application")),
    path('', include('about.urls', namespace="about")),
    path('article/', include('blog.urls', namespace="blog")),
    path('', include('premium.urls', namespace="premium")),

    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Games
    path('Guess_My_Number/', include('Guess_My_Number.urls', namespace="Guess_My_Number")),
    path('Pig_Game/', include('Pig_Game.urls', namespace="Pig_Game")),
    path('Snake_Master/', include('Snake_Master.urls', namespace="Snake_Master")),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
