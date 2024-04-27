import datetime
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import StudentInfo 
from .models import TeacherInfo
from datetime import date
#----------------------------------


def index(request):
     return render(request , 'index.html')

def login_view(request):

     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = authenticate(request, username = username , password = password)
               
          if user is not None:
               login(request,user)
               return redirect('home')
          else:
               return HttpResponse("NO USER AVAILABLE")
               
     return render(request , 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

#----------------------------------


@login_required(login_url='login')
def home(request):
     return render(request , 'home.html')


@login_required(login_url='login')
def newStudentInfo_view(request):

     if request.method == "POST":
          students_name = request.POST.get('students_name')
          mothers_name = request.POST.get('mothers_name')
          fathers_name = request.POST.get('fathers_name')
          students_surname = request.POST.get('students_surname')
          student_photo = request.FILES.get('student_photo')
          
          
          gender = request.POST.get('gender')
          dob = request.POST.get('dob')
          aadhar_no = request.POST.get('aadhar_no')
          
          
          roll_no = request.POST.get('roll_no')
          register_no = request.POST.get('register_no')
          
          
          admission_year = request.POST.get('admission_year')
          academic_year = request.POST.get('academic_year')
          
          
          religion = request.POST.get('religion')
          caste = request.POST.get('caste')
          sub_caste = request.POST.get('sub_caste')
          nationality = request.POST.get('nationality')
          mother_tongue = request.POST.get('mother_tongue')
          state = request.POST.get('state')
          city = request.POST.get('city')
          district = request.POST.get('district')
          taluka = request.POST.get('taluka')
          
          
          street_address = request.POST.get('street_address')
          class_no = request.POST.get('class_no')
          class_division = request.POST.get('class_division')

          # Create a new StudentInfo object and save it to the database
          student_info = StudentInfo(
               user=request.user,
               students_name=students_name,
               mothers_name=mothers_name,
               fathers_name=fathers_name,
               students_surname=students_surname,
               student_photo=student_photo,
               gender=gender,
               dob=dob,
               aadhar_no=aadhar_no,
               roll_no=roll_no,
               register_no=register_no,
               admission_year=admission_year,
               academic_year=academic_year,
               religion=religion,
               caste=caste,
               sub_caste=sub_caste,
               nationality=nationality,
               mother_tongue=mother_tongue,
               state=state,
               city=city,
               district=district,
               taluka=taluka,
               street_address=street_address,
               class_no=class_no,
               class_division=class_division
          )
          student_info.save()
          return redirect('home')

     return render(request , 'student_details/newStudentInfo.html')


@login_required(login_url='login')
def singleStudentSearch_view(request):
     context = {}
     if request.method == 'POST':
          student_name = request.POST.get('student_name')
          student_surname = request.POST.get('student_surname')

          student_info = StudentInfo.objects.filter(user=request.user, students_name = student_name , students_surname = student_surname)
          # print(student_info)
          context = {'student_info':student_info}
     
     return render(request , 'student_details/singleStudentSearch.html' ,context)


@login_required(login_url='login')
def studentDashboard_view(request):
     context = {}
     if request.method == 'POST':
          filters = {}
          class_no = request.POST.get('class_no')
          class_division = request.POST.get('class_division')
          gender = request.POST.get('gender')
          religion = request.POST.get('religion')
          caste = request.POST.get('caste')
          if class_no != 'All':
              filters['class_no'] = class_no
          if class_division != 'All':
              filters['class_division'] = class_division
          if religion != 'All':
              filters['religion'] = religion
          if caste != 'All':
              filters['caste'] = caste
          if gender!= 'All':
               filters['gender'] = gender

          # print(filters)
          students_found = StudentInfo.objects.filter(user=request.user, **filters)
          total_students = students_found.count()
          context = {'students_found': students_found, 'total_students': total_students}
     
     return render(request , 'student_details/studentDashboard.html' ,context)




@login_required(login_url='login')
def updateStudentInfo_view(request, pk):
    student = get_object_or_404(StudentInfo , user=request.user, pk=pk)

    if request.method == "POST":
          student.students_name = request.POST.get('students_name')
          student.mothers_name = request.POST.get('mothers_name')
          student.fathers_name = request.POST.get('fathers_name')
          student.students_surname = request.POST.get('students_surname')
          student.student_photo = request.FILES.get('student_photo')
          
          
          student.gender = request.POST.get('gender')
          student.dob = request.POST.get('dob')
          student.aadhar_no = request.POST.get('aadhar_no')
          
          
          student.roll_no = request.POST.get('roll_no')
          student.register_no = request.POST.get('register_no')
          
          
          student.admission_year = request.POST.get('admission_year')
          student.academic_year = request.POST.get('academic_year')
          
          
          student.religion = request.POST.get('religion')
          student.caste = request.POST.get('caste')
          student.sub_caste = request.POST.get('sub_caste')
          student.nationality = request.POST.get('nationality')
          student.mother_tongue = request.POST.get('mother_tongue')
          student.state = request.POST.get('state')
          student.city = request.POST.get('city')
          student.district = request.POST.get('district')
          student.taluka = request.POST.get('taluka')
          
          
          student.street_address = request.POST.get('street_address')
          student.class_no = request.POST.get('class_no')
          student.class_division = request.POST.get('class_division')


          student.save()
          return redirect('home')

    context = {'student': student}
    return render(request, 'student_details/updateStudentInfo.html', context)







#----------------------------------------------TEACHER'S VIEWS------------------------------------------
@login_required(login_url='login')
def teachersList_view(request):
     teachers_found = TeacherInfo.objects.filter(user=request.user)
     total_teachers = teachers_found.count()
     context = {'teachers_found':teachers_found , 'total_teachers':total_teachers}
     return render(request , 'teacher_details/allTeachersList.html' , context)


@login_required(login_url='login')
def newTeacherInfo_view(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teacher_middle_name = request.POST.get('teacher_middle_name')
        teacher_surname = request.POST.get('teacher_surname')
        teacher_registration_number = request.POST.get('teacher_registration_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        aadhar_no = request.POST.get('aadhar_no')
        teacher_unique_id = request.POST.get('teacher_unique_id')
        teacher_photo = request.FILES.get('teacher_photo')
        teacher_contact_number = request.POST.get('teacher_contact_number')
        qualifications = request.POST.get('qualifications')
        nationality = request.POST.get('nationality')
        mother_tongue = request.POST.get('mother_tongue')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        district = request.POST.get('district')
        taluka = request.POST.get('taluka')
        state = request.POST.get('state')

        teacher_info = TeacherInfo.objects.create(
            user=request.user,
            teacher_name=teacher_name,
            teacher_middle_name=teacher_middle_name,
            teacher_surname=teacher_surname,
            teacher_registration_number=teacher_registration_number,
            gender=gender,
            dob=dob,
            aadhar_no=aadhar_no,
            teacher_unique_id=teacher_unique_id,
            teacher_photo=teacher_photo,
            teacher_contact_number=teacher_contact_number,
            qualifications=qualifications,
            nationality=nationality,
            mother_tongue=mother_tongue,
            street_address=street_address,
            city=city,
            district=district,
            taluka=taluka,
            state=state
        )

        return redirect('home')

    return render(request, 'teacher_details/newTeacherInfo.html')

# import pandas as pd
@login_required(login_url='login')
def todaysBirthdays_view(request):

     today = datetime.date.today()
     todays_birthdays = StudentInfo.objects.filter(dob__day=today.day, dob__month=today.month)
     total_students = todays_birthdays.count()
     print(todays_birthdays)
     context = {'todays_birthdays':todays_birthdays , 'total_students':total_students}

     return render(request, 'student_details/todaysBirthdays.html' , context)