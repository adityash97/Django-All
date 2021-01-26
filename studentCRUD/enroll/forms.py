from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password']
        labels = {'name':'Name','email':'Email','password':'Password'}
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter name here','class':'form-control'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter email here','class':'form-control'}),
            'password':forms.PasswordInput(render_value = True,attrs={'placeholder':'Enter password here','class':'form-control'}),

        }