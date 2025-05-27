from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SpamDetectionLog, Notification

@admin.register(SpamDetectionLog)
class SpamDetectionLogAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'is_spam', 'confidence_score')  # Removed 'detected_at'
    list_filter = ('is_spam',)
    search_fields = ('complaint__complaint_id',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'sent_to', 'sent_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('complaint__complaint_id', 'sent_to__username')
