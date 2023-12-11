from django.contrib import admin
from .models import Student, Faculty, Course,User_DET

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(User_DET)
# Register your models here.
