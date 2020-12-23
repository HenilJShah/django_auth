from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class usercreateform(UserCreationForm):
    """
    here the we create users for our system
    """ 
    # ---------------Meta Data---------------
    class Meta:
        """
        here the fields 
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields = ['first_name', 'last_name', 'email', ]