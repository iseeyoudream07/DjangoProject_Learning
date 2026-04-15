from django.urls import path

from .views import home, topics, topic, new_topic, new_entry, edit_entry, delete_entry, public_topics

app_name = 'learning_app'

urlpatterns = [
    path('', home, name='home'),
    path('topics/', topics, name='topics'),
    path('topics/<int:topic_id>/', topic, name='topic'),
    path('new_topic/', new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>/', delete_entry, name='delete_entry'),
    path('public_topics/', public_topics, name='public_topics'),
]
