from django.contrib import admin
from app.models import ContactEnquiry
from app.models import Signup

class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    
class SignupAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')

admin.site.register(Signup)
admin.site.register(ContactEnquiry)
