# Generated by Django 4.1.4 on 2023-03-11 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_student2_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='student',
            name='date_joined',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
