# Generated by Django 4.1.4 on 2023-03-11 16:28

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_student_date_created_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
