from django.contrib import admin
from myApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    l=['name','usn','subject','marks','email','address']
admin.site.register(Student,StudentAdmin)
