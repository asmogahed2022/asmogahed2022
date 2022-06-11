# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from pyexpat import model
# from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=200)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', )
        
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import BlogModel, User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Email')
    class Meta:
        model = User
        fields = ('username',  'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')



 
class OffersForm(forms.ModelForm):  
    class Meta:  
        model = BlogModel  
        fields = "__all__"