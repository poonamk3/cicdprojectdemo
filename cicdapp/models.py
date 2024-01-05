from django.db import models

class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

   
    student_id = models.CharField(max_length=20, unique=True)
    grade = models.CharField(max_length=10)

    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
