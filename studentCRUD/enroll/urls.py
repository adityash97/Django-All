from django.urls import path
from .views import home,addnshow,updateStudent,deleteStudent
urlpatterns = [
    # path("",home,name= "homePage"),
    path("",addnshow,name="addNshow"),
    path("delete/<int:id>/",deleteStudent,name="deleteStudent"),
    path("<int:id>/",updateStudent,name="updateStudent"),
]
