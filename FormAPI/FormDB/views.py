from django.shortcuts import render
from .forms import UserDetails
from .models import UserDetail

# Create your views here.
def home(request):
    if(request.method == 'POST'):
        ud = UserDetails(request.POST)
        if(ud.is_valid()):
            print("Data from fomr")
            name = ud.cleaned_data['name']
            password = ud.cleaned_data['password']
            email = ud.cleaned_data['email']
            your = ud.cleaned_data['your']
            print("name : {},password :{},email: {},you are{}".format(name,password,email,your))
            # Inserting into database here
            dbObj = UserDetail(name = name,password = password,email = email,your = your)
            dbObj.save()


            return render(request,'FormDB/success.html')
        else:
            return render(request,'FormDB/unsuccessful.html')
    else:
        ud = UserDetails()
        return render(request,'FormDB/home.html',{'form':ud})

    