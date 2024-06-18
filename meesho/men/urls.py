from django.urls import path
from men import views

urlpatterns = [
    
    path('', views.show_men),
    path('add/', views.add_men),
    path('update/', views.update_men)

]
