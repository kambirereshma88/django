

from django.urls import path
from customer_generalform import views

urlpatterns = [
    path('add/', views.add),
]
