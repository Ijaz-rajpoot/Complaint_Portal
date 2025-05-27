from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='student_home'),
    path('live-chat-support.html', views.live_chat_support, name='live_chat_support'),
]
