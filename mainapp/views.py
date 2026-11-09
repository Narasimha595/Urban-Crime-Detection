from django.shortcuts import render,redirect
import urllib.request
import urllib.parse
import random 
import ssl
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from mainapp.models import *

# Create your views here.
def sendSMS(user, otp, mobile):
    data = urllib.parse.urlencode({
        'username': 'Codebook',
        'apikey': '6876b58478ee6ece5fad',
        'mobile': mobile,
        'message': f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.svist.ac.in server. Thank you',
        'senderid': 'CODEBK'
    })
    data = data.encode('utf-8')
    # Disable SSL certificate verification
    context = ssl._create_unverified_context()
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data,context=context)
    return f.read()

def home(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        message=request.POST.get('message')
        Contact_Model.objects.create(yourname=name,youremail=email,phone=phonenumber,Message=message)
        messages.success(request, 'Your message has been submitted successfully.')
        return redirect('contact')
    return render(request,'main/contact.html')

def user(request):
    if request.method=='POST':
        user_email=request.POST.get('email')
        user_password=request.POST.get('password')
        print(user_email,user_password)

        user_data=User_Model.objects.get(email=user_email)
        print(user_data)
        
        if user_data.password==user_password:
            if user_data.otp_status=='verified' and user_data.user_status=='accepted':
                request.session['user_id']=user_data.user_id
                messages.success(request, 'You are logged in..')
                user_data.No_Of_Times_Login += 1
                user_data.save()
                return redirect('user_dashboard')
            elif user_data.otp_status=='verified' and user_data.user_status=='pending':
                messages.info(request, 'Your Status is in pending')
                return redirect('user')
            else:
                messages.warning(request, 'Verify OTP...!')
                request.session['email']=user_data.email
                return redirect('otp')
        else:
            messages.error(request, 'Incorrect Credentials...!')
            return redirect('user')
    return render(request,'main/user.html')

def main_admin(request):
    admin_name = 'admin'
    admin_pwd = 'admin'
    if request.method == 'POST':
        admin_n = request.POST.get('admin_name')
        admin_p = request.POST.get('admin_password')
        if (admin_n == admin_name and admin_p == admin_pwd):
            messages.success(request, 'You are logged in..')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'You are trying to loging with wrong details..')
            return redirect('main_admin')
    return render(request,'main/admin.html')

def registration(request):
    if request.method == "POST":
        fullname = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        age = request.POST.get("age")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        image = request.FILES["image"]
        number = random.randint(1000, 9999)
        print(fullname,email,password,age,address,phone,image)
        try:
            data = User_Model.objects.get(email=email)
            messages.warning(
                request, "Email was already registered, choose another email..!"
            )
            return redirect("registration")
        except:
            sendSMS(fullname, number, phone)
            User_Model.objects.create(
                fullname=fullname,
                email=email,
                phonenumber=phone,
                age=age,
                password=password,
                address=address,
                Image=image,
                otp=number,
            )
            mail_message = (
                f"Registration Successfully\n Your 4 digit Pin is below\n {number}"
            )
            print(mail_message)
            send_mail("User Password", mail_message, settings.EMAIL_HOST_USER, [email])
            request.session["email"] = email
            messages.success(request, "Your account was created..")
            return redirect("otp")
    # Add this line to handle the GET request and render the registration page
    return render(request,'main/registration.html')

def otp(request):
    user_id = request.session['email']
    user_o = User_Model.objects.get(email=user_id)
    print(user_o.otp, 'data otp')

    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        u_otp = int(user_otp)
        if u_otp == user_o.otp:
            user_o.otp_status = 'verified'
            user_o.save()
            messages.success(request, 'OTP verification was Success. Now you can continue to login..!')
            return redirect('user')
        else:
            messages.error(request, 'OTP verification was Faild. You entered invalid OTP..!')
            return redirect('otp')
    return render(request,'main/otp.html')