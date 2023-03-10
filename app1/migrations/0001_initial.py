# Generated by Django 4.1.1 on 2022-12-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Name', models.CharField(max_length=20)),
                ('Emp_ID', models.IntegerField()),
                ('Designtation', models.CharField(max_length=20)),
                ('Date_of_Joining', models.IntegerField()),
                ('Department', models.CharField(max_length=20)),
                ('Salary_Package', models.IntegerField()),
                ('Experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='holidaydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Holidays', models.TextField(max_length=1000)),
                ('Date_of_holidays', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='newsdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Occations', models.TextField(max_length=1000)),
            ],
        ),
    ]
