#create form inheriting from user creation form to add specific inputs
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # gives us nested namespace for configurations
    # user model affected from form.save
    # fields are what we want and in what order
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # allow us to update username or email
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    #allow us to update profile picture
    class Meta:
        model = Profile
        fields = ['image']