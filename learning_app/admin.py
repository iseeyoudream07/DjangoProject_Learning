from django.contrib import admin

# Register your models here.
from learning_app.models import Topic,Entry,Announcement
admin.site.register(Topic)
admin.site.register(Entry)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('content','is_active','updated_at',)
    list_filter = ('is_active',)
