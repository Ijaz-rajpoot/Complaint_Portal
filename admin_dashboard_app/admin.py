from django.contrib import admin
from .models import Department, Assignment, SpamDetectionLog, PriorityAssignment, ChatBotLog, ChatMessage, ChatSession

# Registering models with custom admin views
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head', 'contact_email')  # Reduced to 3 fields
    search_fields = ('name',)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'department', 'assigned_to')  # Reduced to 3 fields
    list_filter = ('department', 'assigned_to')
    search_fields = ('complaint__complaint_id',)

@admin.register(SpamDetectionLog)
class SpamDetectionLogAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'is_spam', 'confidence_score')  # Reduced to 3 fields
    list_filter = ('is_spam',)
    search_fields = ('complaint__complaint_id',)

@admin.register(PriorityAssignment)
class PriorityAssignmentAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'priority_level', 'assigned_by')  # Reduced to 3 fields
    list_filter = ('priority_level',)
    search_fields = ('complaint__complaint_id',)

# ChatBotLog Admin
@admin.register(ChatBotLog)
class ChatBotLogAdmin(admin.ModelAdmin):
    list_display = ('session', 'intent', 'confidence')  # Reduced to 3 fields
    list_filter = ('intent',)
    search_fields = ('session__session_id',)

# ChatMessage Admin
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'sender_type', 'is_read')  # Ensure these fields exist in the model
    list_filter = ('sender_type', 'is_read')  # Ensure these fields exist in the model
    search_fields = ('message',)

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'complaint', 'is_active')  # Ensure these fields exist in the model
    list_filter = ('is_active', 'is_agent_joined')  # Ensure these fields exist in the model
    search_fields = ('session_id', 'complaint__complaint_id')
