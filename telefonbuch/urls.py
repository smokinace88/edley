from django.urls import path
from telefonbuch import views

urlpatterns = [
    path('', views.hello),
    path('einträge/', views.einträge)

]
