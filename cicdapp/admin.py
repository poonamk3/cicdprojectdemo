from django.contrib import admin
from .models import Student,Student_data,Emp,Emp_data
# Register your models here.Student_data
admin.site.register(Student)
admin.site.register(Student_data)
admin.site.register(Emp)
admin.site.register(Emp_data)
