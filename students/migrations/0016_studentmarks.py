# Generated by Django 4.2.2 on 2024-04-22 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0015_teacherinfo_teaacher_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_class', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('what_semester', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('subjects', models.CharField(blank=True, max_length=50, null=True)),
                ('marks', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentinfo')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]