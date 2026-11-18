from django.contrib import admin
from .models import EmergencyContact


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):

    list_display = (
        'contact_name',
        'student',
        'relationship',
        'phone_number',
        'is_primary',
    )

    search_fields = (
        'contact_name',
        'phone_number',
        'student__user__username',
    )

    list_filter = ('relationship', 'is_primary')