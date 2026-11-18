from django.db import models
from students.models import StudentProfile


class EmergencyContact(models.Model):

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='emergency_contacts'
    )

    contact_name = models.CharField(max_length=100)

    relationship = models.CharField(max_length=50)

    phone_number = models.CharField(max_length=20)

    email = models.EmailField(blank=True)

    is_primary = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.contact_name} ({self.relationship})"