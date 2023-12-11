"""AMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.AdminHome,name="Ahome"),
    path("addFaculty",views.add_faculty,name="addFaculty"),
    path("addCourse",views.add_course,name="addCourse"),
    path("addStudent",views.add_student,name="addStudent"),
    path("viewStudent",views.view_student,name="viewstudent"),
    path("viewCourse",views.view_course,name="viewcourse"),
    path("viewFaculty",views.view_faculty,name="viewfaculty"),
    path("updateStudent/<str:student_id>",views.update_student,name="update_student"),
    path("deleteStudent/<str:student_id>",views.delete_student,name="delete_student"),
    path("updateFaculty/<str:faculty_id>",views.update_faculty,name="update_faculty"),
    path("deleteFaculty/<str:faculty_id>",views.delete_faculty,name="delete_faculty"),
    path("updateCourse/<str:course_code>",views.update_course,name="update_course"),
    path("deleteCourse/<str:course_code>",views.delete_course,name="delete_course"),
    path("checklogin",views.check_login,name="checklogin"),
    path("/student-dashboard",views.studentHome,name="Shome"),
    path("/faculty-dashboard",views.facultyHome,name="Fhome"),
]