from django import forms

class UserDetails(forms.Form):
    name = forms.CharField(label = "Name",widget = forms.TextInput(attrs={'placeholder':'Enter your name'}))
    email = forms.EmailField(label = "Email",widget = forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    password = forms.CharField(label = "Password",widget = forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    choices = (
        ("1","Sportsman"),
        ("2","Student"),
        ("3","Programmer"),
        ("4","Others"),
    )
    your = forms.ChoiceField(label = "You are ",choices=choices)

