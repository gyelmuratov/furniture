from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # What columns show in the user list page
    list_display = ('email', 'full_name', 'phone_number', 'is_active', 'created_at')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'full_name', 'phone_number')
    ordering = ('-created_at',)

    # Field layout for the edit/detail page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Field layout for the "Add user" page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'phone_number', 'password1', 'password2'),
        }),
    )