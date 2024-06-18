from django.contrib import admin
from django.urls import path
from train import views as views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.show_train),
    path('update/', views.update_train),
    path('delete/', views.delete_train),
  
]
