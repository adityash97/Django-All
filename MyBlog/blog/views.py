from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title' : "Post 1",
        'author' : "Aditya Anand",
        'type'  : "General",
        'date' : "1.4.2021"
    },{
        'title' : "Post 2",
        'author' : "Aditya ",
        'type'  : "General",
        'date' : "2.4.2021"
    },{
        'title' : "Post 3",
        'author' : "Aditya Sharma",
        'type'  : "Advertisement",
        'date' : "2.4.2021"
    },{
        'title' : "Post 4",
        'author' : "Anand Aditya",
        'type'  : "Personal",
        'date' : "4.4.2021"
    },
    
]
# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello from </h1>")
    context ={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    # return HttpResponse("<h1>This is about response page</h1>")
    return render(request,'blog/about.html')
