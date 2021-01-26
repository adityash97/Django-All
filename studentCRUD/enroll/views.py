from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Create your views here.

#Homepage
def home(request):
    return render(request,'enroll/base.html')

# To add and show data
def addnshow(request):
    if(request.method == 'POST'):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            print("Data i got : \n")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("{},{},{}".format(name,email,password))
            # dbObj = Student(name=name,email=email,password=password)
            # dbObj.save()

            # another way to save data in DB using ModelForm
            form.save()
            # return render(request,'enroll/addNshow.html',{'data':'Check DB!'})
            form = StudentForm()
    else:
        form = StudentForm()
    stud = Student.objects.all()
    return render(request,'enroll/addNshow.html',{'form':form,'data':stud})

# To Update details
def updateStudent(request,id):
    if(request.method == 'POST'):
        student = Student.objects.get(pk = id)
        form = StudentForm(request.POST,instance=student)
        if(form.is_valid()):
            form.save()
    else:
        user = Student.objects.get(pk=id)
        form = StudentForm(instance=user)
    return render(request,'enroll/updateStudent.html',{'form':form})

#To delete data
def deleteStudent(request,id):
    if(request.method == 'POST'):
        stud = Student.objects.get(pk=id)
        stud.delete()
        print("Data is deleted with id : {}".format(id))
        return HttpResponseRedirect("/")