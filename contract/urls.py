from django.urls import path, include
from .views import helloAPI, randomContract

urlpatterns = [
    path('hello/', helloAPI),
    path('<int:id>/', randomContract),
]
