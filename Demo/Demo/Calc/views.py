from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return render(request,'home.html',{'name':'Aditya'})

def result(request):
    input1 = request.POST["firstNumber"]
    input2 = request.POST['secondNumber'] 
    
    result = str(int(input1)+int(input2))
    return render(request,'result.html',{'result':result})
