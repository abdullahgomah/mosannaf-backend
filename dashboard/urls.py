from django.urls import path
from .views import * 

app_name= 'dashboard' 

urlpatterns = [
    path('', dashboard, name='dashboard'), 
    path('getlastfive', get_last_five_mosannaf, name='get-lastfive'),
]