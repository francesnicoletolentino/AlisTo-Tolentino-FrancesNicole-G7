from django.contrib import admin
from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'student_number',
        'user',
        'course',
        'year_level',
    )

    search_fields = (
        'student_number',
        'user__username',
        'user__email',
    )

    list_filter = ('year_level', 'course')