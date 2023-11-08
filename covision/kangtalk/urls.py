from django.urls import path
from .views import user_list, UserCreate

urlpatterns = [
    path('users/', user_list, name='user-list'),  # for listing users or handling GET requests
    path('users/create/', UserCreate.as_view(), name='user-create'),  # for creating a new user with POST
]