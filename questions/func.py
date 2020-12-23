import random
import string
from django.contrib.auth.models import User

def get_random_string(length = 5):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# def userInfo():
#     usr = []
#     for i in User.objects.all():
#         usr.append([i.username])
#     return tuple(usr)