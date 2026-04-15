from .models import Announcement

def global_announcement(request):
    announcements = Announcement.objects.filter(is_active=True).order_by('-updated_at').first()
    return {'site_announcement': announcements}