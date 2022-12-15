"""Web_project_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view),
    path('hr/', views.hr_view),
    path('logout/', views.logout_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Empform/', views.employeeform_view),
    path('EmpData/', views.EmpData_view),
    path('delete/<int:id>', views.delete_view),
    path('update/<int:id>', views.update_view),
    path('AddNews/', views.AddNews_view),
    path('AddCal/', views.AddCal_view),
    path('Emp/', views.Emp_view),
    path('news/', views.news_view),
    path('cal/', views.calender_view),
    path('csv',views.getfile), 

]


''