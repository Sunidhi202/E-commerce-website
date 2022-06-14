from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from users.formss import UserSigninForm
from django.contrib import messages
from . models import MyUser
from getpass import getpass
import string, random
import phonenumbers
import random,sys
import os,math
import smtplib

templatePath = 'users'  

def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1word']

        user = authenticate(email=email, password=password)
        if user is not None:
            print('not none')
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Invalid credentials')
            return render(request, f'{templatePath}/login.html')   
    else:
        return render(request, f'{templatePath}/login.html')        
       
def signup(request):
    try:
        if request.method == 'POST':
            firstname=request.POST.get("firstName", "default value")
            lastname=request.POST.get("lastName", "default value")
            email=request.POST.get("userEmail", "default value")
            password=request.POST.get("pass1", "default value")
            
            username = str(firstname + lastname)

            user = MyUser(username=username, email=email)
            user.first_name = firstname
            user.last_name = lastname
            user.set_password(password)

            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))
            messages = f'click this link to verify your email users/emailVerification'
            send_mail('email verification mail', messages, 'eshop2125@gmail.com', [f'{email}'])
            
            user.save()
            return redirect("/users/login/")
        
        return render(request, f"{templatePath}/signup.html")
    
    except:
        return HttpResponse('Something went wrong :(')


#TODO

# def phoneNumberVerification(request):
#     if request.method == "POST":
#         phoneNumber = request.POST.get('phoneNumberField')
#         if phoneNumber:
#             phoneNumber = '+91'+phoneNumber
#             try:
#                 phoneNumber = phonenumbers.parse(phoneNumber)
#                 if phonenumbers.is_valid_number(phoneNumber):
#                     print(phoneNumber)

#                 else:
#                     messages.error(request, 'Please enter a valid phone number')       
#             except:
#                 messages.error(request, 'Please enter a valid phone number')        
#         else:
#             messages.error(request, 'Phone number is required')

#         return render(request, f"{templatePath}/numberVerification.html")   
#     else:
#         return render(request, f"{templatePath}/numberVerification.html")

def resetpassword(request):
    return render(request, f"{templatePath}/resetpassword.html")    