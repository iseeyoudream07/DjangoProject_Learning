from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'location', 'bio']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your location'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Introduce yourself!'}),
        }
