from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, RegisterForm
from .models import UserProfile


def register_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                f"Welcome aboard, {user.first_name or user.username}! Your account is ready.",
            )
            return redirect('core:home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})
