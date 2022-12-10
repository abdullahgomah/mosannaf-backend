from django.urls import path
from .views import *

app_name = 'mosannaf'


urlpatterns = [
    path('details/<int:id>', details, name='details'),
]
