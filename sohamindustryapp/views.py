from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import companyform2
def index(request):
        return render(request,'index.html')

def weldings(request):
    return render(request,'weldings.html')

def structural(request):
    return render(request,'structural.html')

def heavy(request):
    return render(request,'heavy.html')

def enquiry(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        f_name = request.POST['name']
        f_email = request.POST['email']
        f_comments = request.POST['comments']
        send_mail('Contact Form',
		  f_name, 
		 settings.EMAIL_HOST_USER,
		 ['ranierande331@gmail.com'], 
		 fail_silently=False)
    return render(request,'enquiry.html')
   
def brass(request):
    return render(request,'brass.html')





