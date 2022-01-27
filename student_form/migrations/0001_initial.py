# Generated by Django 3.2.10 on 2022-01-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Student First Name')),
                ('last_name', models.CharField(max_length=60, verbose_name='Student Last Name')),
                ('date_of_birth', models.DateTimeField(verbose_name='Date Of Birth')),
                ('phone', models.CharField(max_length=12, verbose_name='Contact')),
                ('email', models.EmailField(max_length=254, verbose_name='EmailID')),
                ('address', models.CharField(max_length=250, verbose_name='Residence')),
                ('college_name', models.CharField(max_length=100, verbose_name='College Name')),
                ('course', models.CharField(max_length=50, verbose_name='Course Name')),
                ('about', models.TextField(blank=True)),
            ],
        ),
    ]