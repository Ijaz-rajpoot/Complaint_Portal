from django.db import models
from django.shortcuts import render
from django.urls import path
from django.contrib import admin

# Create your models here.

from django.db import models
from student_app.models import Complaint  # Ensure Complaint model is in student_app
from django.contrib.auth.models import User  # For sent_to in Notification

class SpamDetectionLog(models.Model):
    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name='automation_spam_logs'  # Add this line
    )
    is_spam = models.BooleanField(default=False)
    confidence_score = models.FloatField()
    detected_at = models.DateTimeField(auto_now_add=True)  # Add this field

    def __str__(self):
        return f"Spam Detection for {self.complaint.complaint_id}"

class Notification(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    message = models.TextField()
    sent_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification to {self.sent_to} at {self.sent_at}"

def homepage(request):
    return render(request, 'homepage.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),  # URL name is 'homepage'
]

# Add this line to your template file (e.g., homepage.html) where you want the link to appear:
# <a href="{% url 'homepage' %}">Home</a>
