from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from students.models import StudentProfile

User = get_user_model()


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "This email is already registered."
            )

        return email


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(
            email__iexact=email
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "This email is already in use."
            )

        return email


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = [
            'student_number',
            'phone_number',
            'course',
            'year_level',
            'address',
        ]