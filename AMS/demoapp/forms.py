from django import forms
from .models import Student,Faculty,Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['StudentID', 'StudentName', 'Mobile_Number', 'Student_department']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # Add CSS classes and attributes to form fields
        self.fields['StudentID'].widget.attrs.update({'class': 'form-control'})
        self.fields['StudentName'].widget.attrs.update({'class': 'form-control'})
        self.fields['Mobile_Number'].widget.attrs.update({'class': 'form-control'})
        self.fields['Student_department'].widget.attrs.update({'class': 'form-control'})

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['FacultyID', 'FacultyName', 'Mobile_Number', 'Faculty_department']

    def __init__(self, *args, **kwargs):
        super(FacultyForm, self).__init__(*args, **kwargs)
        # Add CSS classes and attributes to form fields
        self.fields['FacultyID'].widget.attrs.update({'class': 'form-control'})
        self.fields['FacultyName'].widget.attrs.update({'class': 'form-control'})
        self.fields['Mobile_Number'].widget.attrs.update({'class': 'form-control'})
        self.fields['Faculty_department'].widget.attrs.update({'class': 'form-control'})

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['CourseCode', 'CourseName', 'Course_Department']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        # Add CSS classes and attributes to form fields
        self.fields['CourseCode'].widget.attrs.update({'class': 'form-control'})
        self.fields['CourseName'].widget.attrs.update({'class': 'form-control'})
        self.fields['Course_Department'].widget.attrs.update({'class': 'form-control'})



class CustomLoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )



