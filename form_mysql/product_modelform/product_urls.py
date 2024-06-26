from django.urls import path
from product_modelform import views

urlpatterns = [
    path('add/', views.add),
]
