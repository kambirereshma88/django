from django.contrib import admin
from django.urls import path
from bus import views as views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.show_bus),
    path('update/', views.update_bus),
    path('delete/', views.delete_bus),
  
]
