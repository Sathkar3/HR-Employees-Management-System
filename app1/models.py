from django.db import models

# Create your models here.

class Employee(models.Model):

	Emp_Name        = models.CharField(max_length=20)

	Emp_ID          = models.IntegerField()

	Designtation    = models.CharField(max_length=20)

	Date_of_Joining = models.IntegerField()

	Department      = models.CharField(max_length=20)

	Salary_Package  = models.IntegerField()

	Experience      = models.IntegerField()



class newsdata(models.Model):

	Occations = models.TextField(max_length=1000)


class holidaydata(models.Model):
	
	Holidays = models.TextField(max_length=1000)
	