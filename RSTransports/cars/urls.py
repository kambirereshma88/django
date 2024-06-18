from django.urls import path
from cars import views

urlpatterns = [
    path('',views.show_cars),
    path('add/', views.add_cars),
    path('update/', views.update_cars),
    
    
]
