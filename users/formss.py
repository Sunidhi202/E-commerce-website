from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import MyUser

class UserSigninForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        def clean_email(self):
            uemail = self.cleaned_data["email"]
            
            for instance in User.objects.all():
                if instance.email == uemail:
                    raise forms.ValidationError('An account with this email already exist')
            return uemail
        