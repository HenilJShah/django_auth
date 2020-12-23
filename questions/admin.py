from django.contrib import admin
from .models import *

# install
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

admin.site.register(feed_que)
# admin.site.register(subject_db)


@admin.register(student_data_db)
class stud_admin(ImportExportModelAdmin):
    list_display = ('fname', 'lname', 'email', 'dob',
                    'contact', 'course', 'sem', 'enrollment_no', 'sem_start', 'create_at')
    pass




@admin.register(subject_db)
class sub_db(ImportExportModelAdmin):
    list_display = ('course_name', 'subject_name', 'subject_code')
    pass
