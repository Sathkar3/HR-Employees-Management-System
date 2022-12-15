from django import forms
from app1.models import Employee
from app1.models import newsdata
from app1.models import holidaydata


class employeeform(forms.ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'
		

class newsform(forms.ModelForm):
	class Meta:
		model = newsdata
		fields = '__all__'


class holidayform(forms.ModelForm):
	class Meta:
		model = holidaydata
		fields = '__all__'

