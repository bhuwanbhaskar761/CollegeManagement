from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    c_name =models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.c_name

class Category(models.Model):
    cat =models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.cat

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username

class Status(models.Model):
    status=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.status


class Student(models.Model):
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    sign = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    gen = models.CharField(max_length=10, null=True)
    add1 = models.CharField(max_length=30, null=True)
    add2 = models.CharField(max_length=30, null=True)
    f_name = models.CharField(max_length=30, null=True)
    m_name = models.CharField(max_length=30, null=True)
    nationality = models.CharField(max_length=30, null=True)
    birth = models.DateField(null=True)
    image = models.FileField(null=True)
    rem_date = models.DateField(null=True)
    rem = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.sign.user.username


class Qualification(models.Model):
    q_name =models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.q_name
class Qualification_detail(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    qualification =models.ForeignKey(Qualification,on_delete=models.CASCADE,null=True)
    year = models.CharField(max_length=10,null=True)
    board = models.CharField(max_length=100,null=True)
    percent = models.CharField(max_length=10,null=True)
    stream = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.qualification.q_name
class Notice(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.TextField(null=True)
    Date1 = models.DateField(null=True)

    def __str__(self):
        return self.title
class Upload_Document(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    tc = models.FileField(null=True)
    mark10 = models.FileField(null=True)
    mark12 = models.FileField(null=True)
    g_certificate = models.FileField(null=True)
    pg_certificate = models.FileField(null=True)

    def __str__(self):
        return self.student.sign.user.username
