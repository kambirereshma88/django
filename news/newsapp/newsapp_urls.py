from django.urls import path
from newsapp import views

urlpatterns = [
    path('', views.base),
    path('politics/',views.politics),
    path('sports/',views.sports),
    path('bollywood/',views.bollywood),

]
