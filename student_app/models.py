from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Under Review', 'Under Review'),
        ('Resolved', 'Resolved'),
        ('Rejected', 'Rejected')
    ]
    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Facilities', 'Facilities'),
        ('Hostel', 'Hostel'),
        ('Administration', 'Administration'),
        ('Other', 'Other')
    ]
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    complaint_id = models.CharField(max_length=10, unique=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='complaints/%Y/%m/%d/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.complaint_id:
            last_id = Complaint.objects.order_by('-id').first()
            self.complaint_id = f"CMP{1000 + (last_id.id if last_id else 0)}"
        super().save(*args, **kwargs)

class Feedback(models.Model):
    RATING_CHOICES = [
        (1, '★ Poor'),
        (2, '★★ Fair'),
        (3, '★★★ Good'),
        (4, '★★★★ Very Good'),
        (5, '★★★★★ Excellent')
    ]
    
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)

# Add these below your existing Complaint and Feedback models

class StatusUpdate(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='status_updates')
    status = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Update for {self.complaint.complaint_id} - {self.status}"


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question


class PortalStats(models.Model):
    total_complaints = models.PositiveIntegerField(default=0)
    resolved_complaints = models.PositiveIntegerField(default=0)
    pending_complaints = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Portal Statistics"


class SupportContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.role}"
