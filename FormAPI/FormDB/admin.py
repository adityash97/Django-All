from django.contrib import admin
from .models import UserDetail
# Register your models here.

@admin.register(UserDetail)
class ModelUserDetails(admin.ModelAdmin):
    list_display =[
        'id','name','password','email','your'
    ]
