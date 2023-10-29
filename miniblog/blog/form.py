from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User

class user_form(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'from-control'}))
    password2 = forms.CharField(label='Confirm Password',  widget=forms.PasswordInput(attrs={'class': 'from-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name',
                  'email': 'Email'
                  }
        widget = {'username': forms.TextInput(attrs={'class': 'from-control'}),
                  'first-name': forms.TextInput(attrs={'class': 'from-control'}),
                  'last_name': forms.TextInput(attrs={'class': 'from-control'}),
                  'email': forms.EmailInput(attrs={'class': 'from-control'})
                  
                  
                  }

#class login_form(AuthenticationForm):
#    pass