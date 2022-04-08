from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

#-----Dynamic Categories Testing
from .models import CategoryStore
choices = CategoryStore.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)
#---------------------------------

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class ProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(label="New Password", max_length = 50,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(label="Repeat New Password",max_length = 50,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))


    class Meta:
        model = User