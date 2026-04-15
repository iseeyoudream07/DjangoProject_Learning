from django.contrib import admin

# Register your models here.
from learning_app.models import Topic,Entry,Announcement

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('txt','date_added','owner','is_public')
    list_editable = ('is_public',)

admin.site.register(Entry)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('content','is_active','updated_at',)
    list_filter = ('is_active',)
