"""second_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from resourcelinks.views import home_screen, east_screen, west_screen, north_screen, south_screen
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home_screen),
    path('admin/', admin.site.urls),
    path('east/', east_screen),
    path('west/', west_screen),
    path('north/', north_screen),
    path('south/', south_screen),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
