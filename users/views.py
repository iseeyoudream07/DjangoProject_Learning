from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from learning_app.models import Topic

# Create your views here.
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
def index(request):
    return render(request, 'learning_app/home.html')

@login_required
def profile(request):
    user = request.user
    topics = Topic.objects.filter(owner=user).order_by('-date_added')
    context = {'user':user,'topics': topics}
    return render(request,'users/profile.html',context)