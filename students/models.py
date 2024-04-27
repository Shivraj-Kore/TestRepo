from django.db import models
from django.contrib.auth.models import User

class StudentInfo(models.Model):
     user = models.ForeignKey( User, on_delete=models.CASCADE , null=True , blank=True)

     students_name = models.CharField(max_length=50 , blank = False , null = False)
     mothers_name = models.CharField(max_length=50 , blank = False , null = False )
     fathers_name = models.CharField(max_length=50 , blank = False , null = False )
     students_surname = models.CharField(max_length=50 , blank = False , null = False )
     #####################for testing , blank=True , null=True###################
     student_photo = models.ImageField(blank=True , null=True) 

     gender_choice = [
          ('m', 'male'),
          ('f', 'female'),
     ]
     gender = models.CharField(max_length=1, choices=gender_choice)
     dob = models.DateField()
     aadhar_no = models.PositiveIntegerField(blank = False , null = False)

#unique----
     roll_no = models.PositiveIntegerField(blank = False , null = False)
     register_no = models.PositiveIntegerField(blank = False , null = False)
#----------
     #####################for testing , blank=True , null=True###################
     admission_year = models.PositiveIntegerField( blank=True , null=True)
     academic_year = models.PositiveIntegerField(blank=True , null=True)

     religion = models.CharField(max_length = 25, blank=True , null=True)
     caste = models.CharField(max_length = 25, blank=True , null=True)
     sub_caste = models.CharField(max_length = 25, blank=True , null=True)

     nationality = models.CharField(max_length = 25, blank=True , null=True)
     mother_tongue = models.CharField(max_length = 20, blank=True , null=True)
     
     state = models.CharField(max_length = 20, blank=True , null=True)
     city = models.CharField(max_length = 20, blank=True , null=True)
     district = models.CharField(max_length = 20, blank=True , null=True)
     taluka = models.CharField(max_length = 20, blank=True , null=True)

     street_address = models.CharField(max_length = 250, blank=True , null=True)

     class_no = models.PositiveIntegerField(blank=True , null=True)
     class_division = models.CharField(max_length=50, blank=True , null=True)

     def __str__(self):
          return  str(self.roll_no)
     
     class Meta:
        # composite unique constraint for roll_no and register_no based on user
        unique_together = ['user', 'roll_no', 'register_no']
     
# class StudentAcademicInfo(models.Model):
#      current_standard = models.CharField(max_length=10)
#      current_division = models.CharField(max_length=10)
     
class TeacherInfo(models.Model):
     user = models.ForeignKey( User, on_delete=models.CASCADE , null=True , blank=True)

     teacher_name = models.CharField(max_length=50)
     teacher_middle_name = models.CharField(max_length=50 , blank=True , null=True)
     teacher_surname = models.CharField(max_length=50)
     teacher_registration_number = models.PositiveIntegerField(blank = False , null = False)
     teacher_unique_id = models.PositiveIntegerField(blank = False , null = False)

     teacher_photo = models.ImageField(blank=True , null=True) 

     gender_choice = [
          ('m', 'male'),
          ('f', 'female'),
     ]
     gender = models.CharField(max_length=1, choices=gender_choice, default='m')
     dob = models.DateField(null=True , blank=True)
     aadhar_no = models.PositiveIntegerField(blank = False , null = False , default=0)
    
     teacher_contact_number = models.PositiveIntegerField(blank=True , null=True)
     
     religion = models.CharField(max_length = 25, blank=True , null=True)
     caste = models.CharField(max_length = 25, blank=True , null=True)
     sub_caste = models.CharField(max_length = 25, blank=True , null=True)

     qualifications = models.CharField(max_length = 25, blank=True , null=True)
     
     nationality = models.CharField(max_length = 25, blank=True , null=True)
     mother_tongue = models.CharField(max_length = 20, blank=True , null=True)

     street_address = models.CharField(max_length = 250, blank=True , null=True)

     state = models.CharField(max_length = 20, blank=True , null=True)
     city = models.CharField(max_length = 20, blank=True , null=True)
     district = models.CharField(max_length = 20, blank=True , null=True)
     taluka = models.CharField(max_length = 20, blank=True , null=True)


     def __str__(self):
         return self.teacher_name
     
     class Meta:
        # composite unique constraint for roll_no and register_no based on user
        unique_together = ['user', 'teacher_unique_id', 'teacher_registration_number']
     


class StudentMarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, null=True, blank=True)
    class_no = models.PositiveSmallIntegerField(blank=True, null=True)
    class_division = models.CharField(max_length=50, blank=True , null=True)
    what_semester = models.PositiveSmallIntegerField(blank=True, null=True)
    subjects = models.CharField(max_length=50, null=True, blank=True)
    marks = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.what_class} : {self.what_semister}"