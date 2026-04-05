from django import forms
from .models import Topic,Entry

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