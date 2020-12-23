from django.db import models
# from .func import userInfo
# Create your models here.


class feed_que(models.Model):
    """
    here the table for feedback que and storing the ans.
    """
    ques = models.CharField(max_length=150)
    admin_id = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class subject_db(models.Model):
    """
    here the 1. course, 2. subject_code, 3. sem
    """
    COURSE = (
        ('BCA-sem-1', 'BCA-sem-1'),
        ('BCA-sem-2', 'BCA-sem-2'),
        ('BCA-sem-3', 'BCA-sem-3'),
        ('BCA-sem-4', 'BCA-sem-4'),
        ('BCA-sem-5', 'BCA-sem-5'),
        ('BCA-sem-6', 'BCA-sem-6'),

        ('MCA-sem-3', 'MCA-sem-3'),
        ('MCA-sem-4', 'MCA-sem-4'),
        ('MCA-sem-5', 'MCA-sem-5'),
        ('MCA-sem-6', 'MCA-sem-6'),
        
        ('BBA-sem-1', 'BBA-sem-1'),
        ('BBA-sem-2', 'BBA-sem-2'),
        ('BBA-sem-3', 'BBA-sem-3'),
        ('BBA-sem-4', 'BBA-sem-4'),
        ('BBA-sem-5', 'BBA-sem-5'),
        ('BBA-sem-6', 'BBA-sem-6'),

        ('MBA-sem-3', 'MBA-sem-3'),
        ('MBA-sem-4', 'MBA-sem-4'),
        ('MBA-sem-5', 'MBA-sem-5'),
        ('MBA-sem-6', 'MBA-sem-6'),
    )
    course_name = models.CharField(max_length=150, choices=COURSE)
    
    subject_name = models.CharField(max_length=150)
    subject_code = models.CharField(max_length=150, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.course_name



class student_data_db(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    dob = models.DateField(auto_now_add=True)
    contact = models.CharField(max_length=150, unique=True)
    course = models.CharField(max_length=150, null=True)
    sem = models.CharField(max_length=150, null=True)


    password = models.CharField(max_length=150)


    enrollment_no = models.CharField(max_length=150, unique=True, null=True)
    sem_start = models.CharField(max_length=150)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.fname


class feedback_question(models.Model):
    """
    feedback_question 
    """
    question_id = models.CharField(max_length=50, unique=True)  # get_random_string(6)
    adminid = models.CharField(max_length=150)
    feedback_question = models.TextField
    create_at = models.DateField(auto_now_add=True)


class student_ans(models.Model):
    """
    student_ans 
    """
    question_id = models.CharField(
        max_length=50, unique=True)  # get_random_string(6)
    studentid = models.CharField(max_length=150)
    enrollment_no = models.CharField(max_length=150)
    student_rating = models.CharField(max_length=150)
    create_at = models.DateField(auto_now_add=True)


class staff_subject(models.Model):
    staff_id = models.CharField(max_length=100)
    course_id = models.CharField(max_length=150)
    subject_code = models.CharField(max_length=150)
    create_at = models.DateField(auto_now_add=True)


# en = 1
# qus = 15fddf
# subject_id = 124
# rating = 3


# 1) Is ashutosh good in practical subject
#  1   2  3  4  5
