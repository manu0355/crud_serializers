from django.db import models

# Create your models here.

class School(models.Model):
    school_name=models.CharField(max_length=50)
    school_branch=models.CharField(max_length=50)
    school_address=models.TextField(max_length=100)

    def __str__(self):
        return self.school_name +" "+ self.school_branch


class Student(models.Model):
    student_name=models.CharField(max_length=40)
    student_rollno=models.IntegerField(null=True)
    student_class=models.CharField(max_length=20,null=True)
    Student_address=models.TextField(max_length=100,null=True)
    school=models.ForeignKey(School,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name+" "+str(self.student_class)