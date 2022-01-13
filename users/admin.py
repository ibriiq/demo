from django.contrib import admin
from .models import userinfo

# Register your models here.

admin.site.register(userinfo)



# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# from .models import User_profile

# # Define an inline admin descriptor for User_profile
# #  model
# # which acts a bit like a singleton
# class UserInline(admin.StackedInline):
#     model = User_profile
#     can_delete = False
#     verbose_name_plural = 'User_profile'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (UserInline,)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)