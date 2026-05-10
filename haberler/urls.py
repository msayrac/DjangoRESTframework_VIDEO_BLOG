
from django.urls import path
from  haberler import views

urlpatterns = [
    path('', views.getHaber),
]
