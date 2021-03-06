# Generated by Django 3.2.3 on 2021-06-16 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
                ('school_branch', models.CharField(max_length=50)),
                ('school_address', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=40)),
                ('student_rollno', models.IntegerField(null=True)),
                ('student_class', models.CharField(max_length=20)),
                ('Student_address', models.TextField(max_length=100)),
                ('school', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='CRUDserial.school')),
            ],
        ),
    ]
