# Generated by Django 4.2.2 on 2024-04-22 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_studentmarks_what_division_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmarks',
            old_name='what_division',
            new_name='class_division',
        ),
        migrations.RenameField(
            model_name='studentmarks',
            old_name='what_class',
            new_name='class_no',
        ),
    ]
