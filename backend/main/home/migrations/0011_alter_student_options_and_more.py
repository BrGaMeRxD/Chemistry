# Generated by Django 4.1.4 on 2023-03-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='date_joined',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='student',
            name='clasa',
            field=models.CharField(choices=[('DAHOM', 'دهم'), ('YAZDAHOM', 'یازدهم'), ('DAVAZDAHOM', 'دوازدهم'), ('FAREGHOLTAHSIH', 'فارغ التحصیل')], default=None, max_length=16),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='code_meli',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
