from django.db import models
from import_export import resources
from .models import student_data_db


class stud_table(resources.ModelResource):
    class Meta:
        model = student_data_db