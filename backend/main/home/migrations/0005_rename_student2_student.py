# Generated by Django 4.1.4 on 2023-03-11 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0004_student2_delete_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student2',
            new_name='Student',
        ),
    ]
