"""
URL configuration for makemytrip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from bus import views as bus_views
from train import views as train_views
from hotels import views as hotels_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hotels/', hotels_views.show_hotels),
    path('update_hotels/', hotels_views.update_hotels),
    path('delete_hotels/', hotels_views.delete_hotels),
    
    path('bus/', bus_views.show_bus),
    path('update_bus/', bus_views.update_bus),
    path('delete_bus/', bus_views.delete_bus),

    path('train/', train_views.show_train),
    path('update_train/', train_views.update_train),
    path('delete_train/', train_views.delete_train),

    #including urls.py from application (folder)
    path('bus/', include('bus.urls')),
    path('hotels/', include('hotels.urls')),
    path('train/', include('train.urls')),

]
