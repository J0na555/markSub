from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Department(models.Model):
    department_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.department_name
    
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length= 50, unique= True)
    description = models.TextField(max_length= 500)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(default= timezone.now)


    def __str__(self):
        return self.course_name
    

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField( max_length=6, choices = GENDER_CHOICES)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default= timezone.now)

    class meta:
        ordering = ['first_name', 'last_name']


    courses = models.ManyToManyField(Course, related_name="students", through='Grade', blank=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Grade(models.Model):
    student = models.ForeignKey(Student,  on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    created_at = models.DateTimeField(default= timezone.now)

    def grade_letter(self):
        if self.grade is None:
            return 'N/A'
        elif self.grade >= 90 and self.grade <= 100:
            return 'A+'
        elif self.grade >= 85 and self.grade <= 89:
            return 'A'
        elif self.grade >= 80 and self.grade <= 84:
            return 'A-'
        elif self.grade >= 75 and self.grade <= 79:
            return 'B+'
        elif self.grade >= 70 and self.grade <= 74:
            return 'B'
        elif self.grade >= 65 and self.grade <= 69:
            return 'B-'
        elif self.grade >= 60 and self.grade <= 64:
            return 'C'
        else:
            return 'F'
        
# checking if the student and the course are in the same department
    def clean(self):
        if self.student.department != self.course.department:
            raise ValidationError('Student and Course must belong to the same Department')

    def save(self,*args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.course}: {self.grade_letter()}"
