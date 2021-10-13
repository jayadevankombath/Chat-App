from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.message_page, name='index'),
    path('add_to_chat/',views.addUserToChat, name='add_user_to_chat'),
]
