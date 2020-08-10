from django.urls import path, include
from .import views
from .import urls


app_name='home'

urlpatterns = [
    path('', views.ho , name='home'),

   
]
