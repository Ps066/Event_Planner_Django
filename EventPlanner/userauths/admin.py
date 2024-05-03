from django.contrib import admin
from userauths.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','username','email','userrole','phone']

admin.site.register(User,UserAdmin)
