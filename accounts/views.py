from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .forms import (
    RegistrationForm,
    UserProfileForm,
    StudentProfileForm
)

from students.models import StudentProfile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your account has been created successfully!"
            )
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


@login_required
def account_home(request):
    if request.user.role == 'ADMIN':
        return redirect('admin_dashboard')

    return redirect('student_dashboard')


@login_required
def student_dashboard(request):
    if request.user.role != 'STUDENT':
        return HttpResponseForbidden(
            "You are not authorized to access this page."
        )

    return render(
        request,
        'accounts/student_dashboard.html'
    )


@login_required
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        return HttpResponseForbidden(
            "You are not authorized to access this page."
        )

    return render(
        request,
        'accounts/admin_dashboard.html'
    )


@login_required
def profile(request):

    user = request.user

    if user.role == 'STUDENT':
        student_profile, created = (
            StudentProfile.objects.get_or_create(user=user)
        )

        if request.method == 'POST':
            user_form = UserProfileForm(
                request.POST,
                instance=user
            )

            student_form = StudentProfileForm(
                request.POST,
                instance=student_profile
            )

            if user_form.is_valid() and student_form.is_valid():
                user_form.save()
                student_form.save()

                messages.success(
                    request,
                    "Your profile has been updated successfully!"
                )

                return redirect('profile')

        else:
            user_form = UserProfileForm(instance=user)
            student_form = StudentProfileForm(
                instance=student_profile
            )

    else:
        student_form = None

        if request.method == 'POST':
            user_form = UserProfileForm(
                request.POST,
                instance=user
            )

            if user_form.is_valid():
                user_form.save()

                messages.success(
                    request,
                    "Your profile has been updated successfully!"
                )

                return redirect('profile')

        else:
            user_form = UserProfileForm(instance=user)

    return render(
        request,
        'accounts/profile.html',
        {
            'user_form': user_form,
            'student_form': student_form,
        }
    )