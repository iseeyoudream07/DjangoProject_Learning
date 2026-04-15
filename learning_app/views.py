from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


def home(request):
    context = {
        'project_name': 'Text Learning',
        'message': 'Welcome to the Text Learning project! This project is designed to help you learn and practice text processing techniques using Django. '
                   'Explore the features and have fun learning!',
        'greet': 'Welcome Back!'
    }
    return render(request, 'learning_app/home.html', context)

def public_topics(request):
    topics = Topic.objects.filter(is_public=True).order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'learning_app/public_topics.html', context)

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'learning_app/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user and not topic.is_public:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_app/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect(reverse('learning_app:topics'))
    context = {'form': form}
    return render(request, 'learning_app/new_topic.html', context)

@login_required
def new_entry(request,topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.author = request.user
            new_entry.save()
            return redirect(reverse('learning_app:topics'))
    context = {'topic': topic,'form': form}
    return render(request, 'learning_app/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if entry.author != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('learning_app:topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form': form}
    return render(request, 'learning_app/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    target_topic_id = entry.topic.id
    if entry.author != request.user:
        raise Http404
    return redirect('learning_app:topic',topic_id=target_topic_id)