from django.urls import path
from product import views

urlpatterns = [
    path('show/', views.show),
    path('add/', views.add),
    path('update/', views.update),
]
