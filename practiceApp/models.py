from django.db import models

# Create your models here.


class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    gender_male = 0
    gender_female = 1
    gender_choice = [(gender_male, 'Male'), (gender_female, 'Female')]
    gender = models.IntegerField(choices=gender_choice)
    pasword= models.CharField(max_length=100)
    re_password=models.CharField(max_length=100)



    def __str__(self):
        return self.first_name
