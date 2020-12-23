from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# models
from .models import student_data_db

# create own deco.
from .rols_deco import unauthenticated_user, allowed_users, admin_only

# usercreate forms
from .forms import usercreateform


# dashboard
# @login_required(login_url='student_data')
@allowed_users(allowed_rolles=['admin', 'staff'])
def home(request):
    mca_total = student_data_db.objects.filter(course = 'Mca').count()
    mba_total = student_data_db.objects.filter(course = 'Mba').count()
    bca_total = student_data_db.objects.filter(course = 'Bca').count()
    bba_total = student_data_db.objects.filter(course = 'Bba').count()
    data = student_data_db.objects.all()
    data_transfer = {
        'mca':mca_total,
        'mba':mba_total,
        'bba':bba_total,
        'bca':bca_total,
        'student': data
    }
    return render(request, "accounts/index.html", data_transfer)


# staff login
@unauthenticated_user
def staff_login(request):
    staff_name = request.POST.get('staff_name')
    staff_password = request.POST.get('staff_password')
    print(f'\n{staff_name}, \n{staff_password}\n')

    user = authenticate(request, username=staff_name, password=staff_password)
    print(f'\n\n\n\n{user}\n\n\n\n')
    if request.method == 'POST':
        if user is not None:
            print('\n\n\n\nif user\n\n\n\n')
            login(request, user)
            return redirect('home')
        else:
            print('\n\n\n\nelse user\n\n\n\n')
            messages.info(request, 'please check your username and password')
    return render(request, 'accounts/staff_login.html')


# staff logout
def userlogout(request):
    logout(request)
    return redirect('staff_login')


# userRegistration
# @unauthenticated_user
@allowed_users(allowed_rolles=['admin'])
def userRegistration(request):
    form = usercreateform()
    if request.method == 'POST':
        form = usercreateform(request.POST)
        if form.is_valid():
            user = form.save()
            # print(f'\n\n{username}\n\n')
            group = Group.objects.get(name='staff')
            # print(f'\n\n{group}\n\n')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, "Thank you for your registration! Your account is now ready to use.\t" + username)
            # return redirect('staff_login')
    return render(request, 'accounts/register.html', {'reg_form': form})


# stud login
def student_data(request):
    student_enroll_no = request.POST.get('student_id')
    student_password = request.POST.get('student_password')

    if request.method == "POST":
        print(f'\n\n\nif part post request\n\n\n')
        if student_data_db.objects.filter(enrollment_no=student_enroll_no, password=student_password):
            student = student_data_db.objects.get(enrollment_no=student_enroll_no, password=student_password)    

            print(f'\n\n\nif part post request and >if inside if part\n\n\n')
            print(f'\n\n\n{student}\n\n\n')
            request.session['student'] = [student.id, student.fname, student.lname, student.email, student.contact, student.course, student.enrollment_no]
            return render(request, 'accounts/student_welcome.html', {'name':student})

        else:
            print(f'\n\n\nif part post request > if inside else part\n\n\n')
            messages.info(request, 'places chack your carendical information')
            return redirect('student_data')    

    if request.session.has_key('student'):
        print(f'\n\n\nif session is create\n\n\n')
        name = request.session.get('student')[1]
        return render(request, 'accounts/student_welcome.html', {'name': name})
    else:
        print(f'\n\n\nelse session not create\n\n\n')
        return render(request, 'accounts/student_login.html')

# stud_logout
def logout_student(request):
    request.session.flush()
    request.session.clear_expired()
    return redirect('student_data')


