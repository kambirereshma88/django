from django.urls import path
from bus import views

urlpatterns = [
    path('', views.show_bus),
    path('add/', views.add_bus),
    path('update/', views.update_bus),
    
]
