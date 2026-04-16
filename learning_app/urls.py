from django.urls import path

from .views import home, topics, topic, new_topic, new_entry, edit_entry, delete_entry, public_topics, \
    toggle_topic_public, edit_announcement

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
    path('topic/<int:topic_id>/toggle_public', toggle_topic_public, name='toggle_topic_public'),
    path('announcement/edit/',edit_announcement,name='edit_announcement'),
]
