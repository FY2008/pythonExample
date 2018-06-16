from django.urls import path, include
from .views import profile

app_name = 'users'
urlpatterns = [
    path('profile/', profile, name='profile'),
]
