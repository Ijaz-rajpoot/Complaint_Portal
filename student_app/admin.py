from django.contrib import admin
from .models import Complaint, StatusUpdate, FAQ, Feedback, PortalStats, SupportContact

# Registering the models with the admin interface
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('complaint_id', 'title', 'category', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description', 'complaint_id')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'rating', 'submitted_at', 'is_anonymous')

# These models can still be registered directly if needed:
admin.site.register(StatusUpdate)
admin.site.register(FAQ)
admin.site.register(PortalStats)
admin.site.register(SupportContact)
