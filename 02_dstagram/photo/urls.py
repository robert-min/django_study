from django.urls import path

from .views import *

app_name = "photo"

urlpatterns = [
    path('', photo_list, name="photo_list"),
]