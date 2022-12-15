from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from app1.forms import employeeform, newsform, holidayform
from app1.models import Employee, newsdata, holidaydata
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv

# Create your views here.

def home_view(request):
	return render(request,'app1/home.html')


@login_required
def hr_view(request):
	return render(request,'app1/hr.html')


def employeeform_view(request):
	form=employeeform()
	if request.method=="POST":
		form=employeeform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/EmpData')
	return render(request,'app1/hrform.html',{'f':form})


def EmpData_view(request):
	employee=Employee.objects.all()
	return render(request,'app1/EmpData.html',{'e':employee})


def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/EmpData')


def update_view(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=="POST":
		form=employeeform(request.POST,instance=employee)
		if form.is_valid():
			form.save()
			return redirect('/EmpData')
	return render(request,'app1/update.html',{'employee':employee})



def getfile(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="file.csv"'
	employees = Employee.objects.all()  
	writer = csv.writer(response)  
	writer.writerow(['Emp_Name', 'Emp_ID ','Designtation','Date_of_Joining','Department','Salary_Package','Experience'])
	for i in employees:
		writer.writerow([i.Emp_Name,i.Emp_ID,i.Designtation,i.Date_of_Joining,i.Department,i.Salary_Package,i.Experience])
		return response  


def logout_view(request):
	auth.logout(request)
	return render(request,'app1/logout.html')


def AddNews_view(request):
	news=newsform()
	if request.method=="POST":
		form=newsform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/news')
	return render(request,'app1/AddNews.html',{'ne':news})


def AddCal_view(request):
	holiday=holidayform()
	if request.method=="POST":
		form=holidayform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/cal')
	return render(request,'app1/AddCal.html',{'ho':holiday})


def Emp_view(request):
	return render(request,'app1/Emp.html')



def news_view(request):
	news=newsdata.objects.all()
	return render(request,'app1/news.html',{'n':news})


def calender_view(request):
	holidays=holidaydata.objects.all()
	return render(request,'app1/calendar.html',{'h':holidays})




