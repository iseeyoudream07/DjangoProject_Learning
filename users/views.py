from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from learning_app.models import Topic
from .forms import ProfileForm


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_app:home')
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    profile_obj = request.user.profile
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {
        'profile': profile_obj,
        'topics': topics,
    }
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    profile_obj = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(instance=profile_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=profile_obj)
    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)
