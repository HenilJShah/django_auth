from django.http import HttpResponse
from django.shortcuts import redirect


# unauthenticated_user
def unauthenticated_user(view_file_params):
    def wrapper_func(request, *args, **kwargs):
        # logic part
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_file_params(request, *args, **kwargs)
    return wrapper_func



# rolles
def allowed_users(allowed_rolles = []):
    def deco(view_file_params):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                # print('\nrolles->>>>> here the chack it \n', allowed_rolles)
                group = request.user.groups.all()[0].name
                # print(group)
            if group in allowed_rolles:
                # print('\nrolles is allowrd\n', allowed_rolles)
                return view_file_params(request, *args, **kwargs)
            else:
                # print('\nrolles here is not allowed\n', allowed_rolles)
                # return HttpResponse('you are not authorized to views this page')
                return redirect('student_data')
        return wrapper_func
    return deco



# admin only
def admin_only(view_file_params):
    def wrapper_func(request, *args, **kwargs):
        
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'students':
            return redirect('home')

        if group == 'admin' or group == 'staff':
            return view_file_params(request, *args, **kwargs)
        
    return wrapper_func




