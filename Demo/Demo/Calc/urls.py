from django.urls import path
from .views import homePage
from .views import result

urlpatterns = [
    path('',homePage,name="home"),
    path('result',result,name="result")
]