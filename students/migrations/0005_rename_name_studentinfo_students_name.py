# Generated by Django 4.2.2 on 2024-03-31 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_studentinfo_academic_year_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='name',
            new_name='students_name',
        ),
    ]
