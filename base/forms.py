from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *


# Reordering Form and View
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        Profile.objects.create(user=user)
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'city', 'state', 'zipcode', 'phone')


class PositionForm(forms.Form):
    position = forms.CharField()
