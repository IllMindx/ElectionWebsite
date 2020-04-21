from django import forms
from django.forms import ModelForm
from .models import Candidate, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class LoginForm(forms.ModelForm):
    card_id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['card_id', 'password']
    
    def clean(self):
        if self.is_valid():
            card_id = self.cleaned_data['card_id']
            password = self.cleaned_data['password']
            if not authenticate(card_id=card_id, password=password):
                raise forms.ValidationError('Invalid login')


class VoteForm(forms.Form):
    candidate_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'candidate_number',
            'onchange': 'change_img()'
            }
        )
    )


class UserForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['name', 'email', 'card_id']
