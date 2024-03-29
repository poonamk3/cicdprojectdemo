# Generated by Django 3.2.23 on 2024-01-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='cccc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='dddd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('grade', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
    ]
