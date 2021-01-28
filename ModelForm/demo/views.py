from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
# Create your views here.

def home(request):
    return render(request,'demo/home.html')

def login(request):
    if(request.method == 'POST'):
        form = Login(request.POST)
        if(form.is_valid()):
            print("Data from login form")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("Email : {}  Password : {}".format(email,password))
            # Check for email and password in data base
            return HttpResponse("<h1> Successfull !  To signin :  http://localhost:8000/signup/ </h1><h2> Email : {} Password : {}</h2>".format(email,password))
    else:
        form = Login()    
    return render(request,'demo/login.html',{'form':form})

def signup(request):
    if(request.method == 'POST'):
        form = Signup(request.POST)
        if(form.is_valid()):
            print("Data from login form")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("Name : {} Email : {}  Password : {} ".format(name ,email,password))
            form.save()
            return HttpResponse("<h1> Signup Successfull ! You can Login in:  http://localhost:8000/login/ </h1><h2> Email : {} Password : {}</h2>".format(email,password))
    else:
        form = Signup()    
    return render(request,'demo/signup.html',{'form':form})
