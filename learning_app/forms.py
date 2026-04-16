from django import forms
from .models import Topic,Entry,Announcement

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['txt']
        labels = {'txt':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['txt']
        labels = {'txt':''}
        widgets = {'txt':forms.Textarea(attrs={'cols':80})}

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['content','is_active']
        labels = {'content':'Announcement Content','is_active':'Show on frontend?'}
        widgets = {'content':forms.Textarea(attrs={'cols':80,'class':'form-control'})}