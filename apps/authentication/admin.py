from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'password')

    def username(self, obj):
        return obj.username
    
    def email(self, obj):
        return obj.email
    
    def fname(self, obj):
        return obj.first_name
    
    def lname(self, obj):
        return obj.last_name
    
    def password(self, obj):
        return obj.password
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)