from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.chat_page,
        name='chatbot'
    ),

    path(
        'send/',
        views.send_message,
        name='send_message'
    ),

]