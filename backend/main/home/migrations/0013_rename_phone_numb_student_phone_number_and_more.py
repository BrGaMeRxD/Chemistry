# Generated by Django 4.1.4 on 2023-03-11 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_phone_number_student_phone_numb_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phone_numb',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='user_name',
            new_name='username',
        ),
    ]