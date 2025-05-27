from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

# Create your views here.

from django.shortcuts import render

def live_chat_support(request):
    return render(request, 'live-chat-support.html')
