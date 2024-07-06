from django.urls import path
from myapp import views

urlpatterns = [
    path('register/',views.register),
    path('home/',views.home),
    path ('login/',views.user_login),
    path('logout/',views.user_logout),
]