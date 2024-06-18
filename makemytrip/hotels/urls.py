
from django.contrib import admin
from django.urls import path
from hotels import views as views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.show_hotels),
    path('update/', views.update_hotels),
    path('delete/', views.delete_hotels),
  
]