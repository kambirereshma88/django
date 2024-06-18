from django.urls import path
from customer import views

urlpatterns = [
    path('', views.show_customer),
    path('update/',views.update_customer),
    path('delete/',views.delete_customer)
]