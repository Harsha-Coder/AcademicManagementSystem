from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Faculty, Course, User_DET
from .forms import StudentForm, FacultyForm, CourseForm, CustomLoginForm

def AdminHome(request):
    return render(request,"demoapp/Adminbase.html",)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
             # Redirect to a success page
    else:
        form = StudentForm()

    return render(request, 'demoapp/addStudent.html', {'form': form})

def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page
    else:
        form = FacultyForm()

    return render(request, 'demoapp/addFaculty.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page
    else:
        form = CourseForm()

    return render(request, 'demoapp/addCourse.html', {'form': form})

def view_student(request):
    students = Student.objects.all()
    count = Student.objects.count()
    return render(request, 'demoapp/viewStudent.html', {'students': students, 'count': count})

def view_faculty(request):
    faculties = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, 'demoapp/viewFaculty.html', {'faculties': faculties, 'count': count})

def view_course(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, 'demoapp/viewCourse.html', {'courses': courses, 'count': count})

def update_student(request, student_id):
    student = get_object_or_404(Student, StudentID=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('viewstudent')
    else:
        form = StudentForm(instance=student)

    return render(request, 'demoapp/UpdateStudent.html', {'form': form, 'student': student})

def update_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, FacultyID=faculty_id)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('viewfaculty')
    else:
        form = FacultyForm(instance=faculty)

    return render(request, 'demoapp/UpdateFaculty.html', {'form': form, 'faculty': faculty})
def delete_student(request, student_id):
    student = get_object_or_404(Student, StudentID=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('viewstudent')

    return render(request, 'demoapp/deletestudent.html', {'student': student})


def delete_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, FacultyID=faculty_id)

    if request.method == 'POST':
        faculty.delete()
        return redirect('viewfaculty')

    return render(request, 'demoapp/deletefaculty.html', {'faculty': faculty})


def delete_course(request, course_code):
    course = get_object_or_404(Course, CourseCode=course_code)

    if request.method == 'POST':
        course.delete()
        return redirect('viewcourse')

    return render(request, 'demoapp/deletecourse.html', {'course': course})


def update_course(request, course_code):
    course = get_object_or_404(Course, CourseCode=course_code)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('viewcourse')
    else:
        form = CourseForm(instance=course)

    return render(request, 'demoapp/UpdateFaculty.html', {'form': form, 'course': course})

def login(request):
    form = CustomLoginForm()
    return render(request,"demoapp/login.html",{'form':form})

def studentHome(request):
    return render(request,"demoapp/Studentbase.html")

def facultyHome(request):
    return render(request,"demoapp/Facultybase.html")
def check_login(request):
    adminuname = request.POST.get("username")
    adminpwd = request.POST.get("password")

    if adminuname and adminpwd:
        # Use get() instead of filter() to get a single object
        user = User_DET.objects.filter(
            (Q(adminusr=adminuname)|Q(faculty_id=adminuname) | Q(student_id=adminuname)) & Q(password=adminpwd)).first()

        if user:
            if user.role == "admin":
                return redirect("Ahome")
            elif user.role == "student":
                return redirect("Shome")
            elif user.role == "faculty":
                return redirect("Fhome")
            else:
                return HttpResponse("Invalid role")
        else:
            return HttpResponse("Invalid username or password")
    else:
        return HttpResponse("Data not received correctly")


# Create your views here.
