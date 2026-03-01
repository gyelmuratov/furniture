from django.contrib import admin
from django.contrib import admin

from shared.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'is_read', 'created_at']
    search_fields = ['full_name', 'email', 'subject', 'message']
    list_filter = ['is_read', 'created_at']