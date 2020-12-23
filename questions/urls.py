from django.urls import path
from . import views

urlpatterns = [
    # pages
    path('',views.home, name='home'),

    # login
    path('staff_login/',views.staff_login, name='staff_login'),
    path('student_data/',views.student_data, name='student_data'),


    # logout
    path('userlogout/',views.userlogout, name='userlogout'),
    path('logout_student/',views.logout_student, name='logout_student'),

    # userRegistration
    path('userRegistration/',views.userRegistration, name='userRegistration'),
]
