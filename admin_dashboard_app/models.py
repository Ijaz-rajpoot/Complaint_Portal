from django.db import models
from django.contrib.auth.models import User
from student_app.models import Complaint  # Ensure that this import is correct

# ChatBotLog Model
class ChatBotLog(models.Model):
    session = models.ForeignKey('ChatSession', on_delete=models.CASCADE)
    intent = models.CharField(max_length=100)
    confidence = models.FloatField()

    def __str__(self):
        return f"Session: {self.session}, Intent: {self.intent}"

# ChatMessage Model
class ChatMessage(models.Model):
    message = models.TextField()
    sender_type = models.CharField(max_length=20)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message by {self.sender_type}"

class ChatSession(models.Model):
    session_id = models.CharField(max_length=100)
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_agent_joined = models.BooleanField(default=False)  # Added field

    def __str__(self):
        return f"Session {self.session_id} - Active: {self.is_active}"


# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

# Assignment Model
class Assignment(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Assignment for {self.complaint.complaint_id}"

# SpamDetectionLog Model
class SpamDetectionLog(models.Model):
    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name='admin_spam_logs'  # Add this line
    )
    is_spam = models.BooleanField(default=False)
    confidence_score = models.FloatField()

    def __str__(self):
        return f"Spam Detection for {self.complaint.complaint_id}"

# PriorityAssignment Model
class PriorityAssignment(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]

    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name='priority_assignments'  # Add this line
    )
    priority_level = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Priority {self.priority_level} for {self.complaint.complaint_id}"
