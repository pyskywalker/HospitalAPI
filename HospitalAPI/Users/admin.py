from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,UserType,HospitalRoom
# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields=('username','first_name','last_name')
    list_filter=('username','is_active','is_staff')
    ordering=('username',)
    list_display=('username','is_active','is_staff')

    fieldsets=((None, {'fields':('username','password','usertype','first_name','last_name','room')}),
    ('Permissions',{'fields':('is_staff','is_active')}),
    ('Personal',{'fields':('description','phone')}))

admin.site.register(User,UserAdminConfig)
mymodels=[UserType,HospitalRoom]
for model in mymodels:
    admin.site.register(model)