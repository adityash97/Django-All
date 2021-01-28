from django import forms
from .models import User

class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

        widgets = {
            'email':forms.TextInput(attrs={'placeholder' : 'Enter email here'}),
            'password':forms.PasswordInput(attrs={'placeholder' : 'Enter password here'}),
        }

    def clean_email(self):
        value = self.cleaned_data['email']
        dbEmail  = ""
        try:
            dbEmail = User.objects.get(email = value)
        except:
            pass
        if(dbEmail == ""):
            raise forms.ValidationError('Check Username or password!')
        return value

class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
    
        widgets = {
        'name':forms.TextInput(attrs={'placeholder' : 'Enter name here'}),
        'email':forms.TextInput(attrs={'placeholder' : 'Enter email here'}),
        'password':forms.TextInput(attrs={'placeholder' : 'Enter password here'}),
    }


    def clean_email(self):
        value = self.cleaned_data['email']
        dbEmail  = ""
        try:
            dbEmail = User.objects.get(email = value)
        except:
            pass
        if(dbEmail != ""):
            raise forms.ValidationError('Email Already exist.Use differnt')
        return value