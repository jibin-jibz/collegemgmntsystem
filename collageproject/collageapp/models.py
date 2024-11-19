from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USERTYPE=models.CharField(max_length=100)

class Departmnet(models.Model):
    Deparname=models.CharField(max_length=50)


class Teacher(models.Model):
    Depar_id=models.ForeignKey(Departmnet,on_delete=models.CASCADE)
    tid=models.ForeignKey(User,on_delete=models.CASCADE)
    Age=models.IntegerField()
    Address=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=50)

class Student(models.Model):
    Depar_id=models.ForeignKey(Departmnet,on_delete=models.CASCADE)
    sid=models.ForeignKey(User,on_delete=models.CASCADE)
    Age=models.IntegerField()
    Address=models.CharField(max_length=100)

    