# Generated by Django 4.2.2 on 2024-04-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_alter_studentinfo_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='register_no',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='roll_no',
            field=models.PositiveIntegerField(),
        ),
    ]
