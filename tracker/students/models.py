from django.db import models



class Department(models.Model):
    department_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.department_name
    
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length= 50, unique= True)
    description = models.TextField(max_length= 500)

    def __str__(self):
        return self.course_name
    

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField( max_length=50, choices = GENDER_CHOICES)
    email = models.EmailField(unique=True)

    courses = models.ManyToManyField(Course, related_name="students", through='Grade', blank=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Grade(models.Model):
    student = models.ForeignKey(Student,  on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.student} - {self.course}:{self.grade}"
