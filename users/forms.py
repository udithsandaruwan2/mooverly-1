from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Profile, StaffCode

class CustomUserCreationForm(UserCreationForm):
    staff_code = forms.CharField(max_length=200, required=True, help_text="Enter your staff code")
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2', 'staff_code']
        labels = {
            'first_name':'Name', 
        }
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': 'eg : Udith Sandaruwan', 'type':'text'},
        )

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder':'eg : udith@eventarc.com', 'type':'text'}
        )

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': 'eg : udith002', 'type':'text'}
        )

        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': '*************', 'type':'password'}
        )

        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': '*************', 'type':'password'}
        )
        
        self.fields['staff_code'].widget.attrs.update(
            {'class': 'form-control form-control-xl', 'placeholder': 'SHOP00XX', 'type':'password'}
        )

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'short_intro', 'bio',
                'profile_image']
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['location'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['short_intro'].widget.attrs.update(
            {'class': 'form-control'}
        )
        
        self.fields['bio'].widget.attrs.update(
            {'class': 'form-control'}
        )

        self.fields['profile_image'].widget.attrs.update(
            {'class': 'form-control', 'id':'formFile'}
        )
        
