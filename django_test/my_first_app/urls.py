from django.urls import path
from .views import my_first_view

urlpatterns = [
    path('my_first_view/', my_first_view, name='my_first_view'),
]
