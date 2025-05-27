# from django.contrib import admin
# from django.urls import path
# from django.views.generic import TemplateView

# urlpatterns = [
#     path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
   
# ]

from django.contrib import admin
from django.urls import path, include  # include added
from django.shortcuts import render
from django.contrib.auth import views as auth_views

def contact_view(request):
    return render(request, 'contact_page.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact_view, name='homepage'),
    path('contact/', contact_view, name='contact'),
    path('student_app/', include('student_app.urls')),  # ✅ Add this line to include your app's routes
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]


