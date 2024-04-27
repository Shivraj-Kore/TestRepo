from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , views.index , name='index'),
    path('login/' , views.login_view , name='login'),
    path('home/' , views.home , name='home'),
    path('logout/' , views.logout_view , name='logout'),
    path('newStudentInfo/' , views.newStudentInfo_view , name='newStudentInfo'),
    path('singleStudentSearch/' , views.singleStudentSearch_view , name='singleStudentSearch'),
    path('studentDashboard/' , views.studentDashboard_view , name='studentDashboard'),
    path('updateStudentInfo/<int:pk>' , views.updateStudentInfo_view , name='updateStudentInfo'),
    path('todaysBirthdays' , views.todaysBirthdays_view , name='todaysBirthdays'),
    
    # --------------Teacher's urls----------------
    path('newTeacherInfo/' , views.newTeacherInfo_view , name='newTeacherInfo'),
    path('teachersList/' , views.teachersList_view , name='teachersList'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)