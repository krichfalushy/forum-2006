from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class SignUpForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit)
        author_group = Group.objects.get(name='Author')
        user.groups.add(author_group)
        return user
