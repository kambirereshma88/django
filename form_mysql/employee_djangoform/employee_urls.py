from django.urls import path
from employee_djangoform import views

urlpatterns = [
    path('add/', views.add),
]
