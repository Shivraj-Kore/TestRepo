# Generated by Django 4.2.2 on 2024-04-02 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_rename_name_studentinfo_students_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='surname',
            new_name='student_surname',
        ),
    ]