from django.urls import path
from women import views

urlpatterns = [
    
    path('', views.show_women),
    path('add/', views.add_women),
    path('update/', views.update_women)

]
