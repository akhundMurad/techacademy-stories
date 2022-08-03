from django import forms

from blog.models import Category


class SubscribeToNewletter(forms.Form):
    email = forms.EmailField(
        max_length=128,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter your email"}),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(posts__isnull=False).distinct("id"),
        label="",
    )
