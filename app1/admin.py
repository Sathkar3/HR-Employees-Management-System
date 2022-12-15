from django.contrib import admin
from app1.models import Employee, newsdata, holidaydata

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
	list_display=['Emp_Name','Emp_ID','Designtation','Date_of_Joining','Department','Salary_Package','Experience']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(newsdata)
admin.site.register(holidaydata)
