from django.urls import path
from .views import home,login,signup
urlpatterns =[
    path('',home,name = 'model-home'),
    path('login/',login,name= 'model-login'),
    path('signup/',signup,name = 'model-signup')
]