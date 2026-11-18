
from django.conf import settings
from django.db import models


class StudentProfile(models.Model):

    class YearLevel(models.TextChoices):
        FIRST = '1st Year', '1st Year'
        SECOND = '2nd Year', '2nd Year'
        THIRD = '3rd Year', '3rd Year'
        FOURTH = '4th Year', '4th Year'
        FIFTH = '5th Year', '5th Year'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )

    student_number = models.CharField(
        max_length=30,
        unique=True,
        null=True,
        blank=True
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    course = models.CharField(
        max_length=100,
        blank=True
    )

    year_level = models.CharField(
        max_length=20,
        choices=YearLevel.choices,
        blank=True
    )

    address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
