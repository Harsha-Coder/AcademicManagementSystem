from django.db import models
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    StudentID = models.BigIntegerField(primary_key=True)
    StudentName = models.CharField(max_length=200,blank=False)
    Mobile_Number = models.BigIntegerField(blank=False)
    department_choices = (("CSE-H", "CSE(HOUNORS)"), ("CSE-R", "CSE(REGULARS)"),("ECE", "ECE"),("BT", "BT"), ("CS-IT","CS-IT"),("AI&DS","AI&DS"))
    Student_department = models.CharField(max_length=200,blank=False,choices=department_choices)


    def __str__(self):
        return str(self.StudentID)

class Faculty(models.Model):
    FacultyID = models.BigIntegerField(primary_key=True)
    FacultyName = models.CharField(max_length=200,blank=False)
    Mobile_Number = models.BigIntegerField(blank=False)
    department_choices = (("CSE","CSE"),("ECE","ECE"),("BT","BT"))
    Faculty_department = models.CharField(max_length=200,blank=False,choices=department_choices)

    def __str__(self):
        return str(self.FacultyID)

class Course(models.Model):
    CourseCode = models.CharField(primary_key=True,max_length=200,blank=False)
    CourseName = models.CharField(max_length=100,blank=False)
    department_choices = (("CSE-H", "CSE(HOUNORS)"), ("CSE-R", "CSE(REGULARS)"), ("ECE", "ECE"), ("BT", "BT"), ("CS-IT", "CS-IT"),("AI&DS","AI&DS"))
    Course_Department = models.CharField(max_length=200,blank=False,choices=department_choices)

    def __str__(self):
        return str(self.CourseCode)


class User_DET(models.Model):

    adminusr = models.CharField(max_length=100,null=True,blank=True)

    student_id = models.OneToOneField(
        'Student',
        on_delete=models.CASCADE,
        related_name='user_student',
        blank=True,
        null=True,
        default=None,
    )

    faculty_id = models.OneToOneField(
        'Faculty',
        on_delete=models.CASCADE,
        related_name='user_faculty',
        blank=True,
        null=True,
        default=None,
    )

    role_choices = (
        ('unknown', 'Unknown'),
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=20, choices=role_choices, default='unknown')

    password = models.CharField(max_length=100,blank=False,default="klu@123")

    def __str__(self):
        if self.student_id:
            return f"Student: {self.student_id} ({self.role})"
        elif self.faculty_id:
            return f"Faculty: {self.faculty_id} ({self.role})"
        else:
            return f"{self.adminusr} ({self.role})"

@receiver(post_save, sender=Student)
def create_user_det_for_student(sender, instance, created, **kwargs):
    if created:
        User_DET.objects.create(student_id=instance, role='student')

# Signal to create User_DET instance after Faculty instance is saved
@receiver(post_save, sender=Faculty)
def create_user_det_for_faculty(sender, instance, created, **kwargs):
    if created:
        User_DET.objects.create(faculty_id=instance, role='faculty')
