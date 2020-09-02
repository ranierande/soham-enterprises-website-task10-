from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
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
        fname = request.POST['name']
        femail = request.POST['email']
        message = request.POST['message']

        send_mail('Contact Form',
		 message, 
		 settings.EMAIL_HOST_USER,
		 ['ranierande331@gmail.com'], 
		 fail_silently=False)
    return render(request,'enquiry.html')
   
def brass(request):
    return render(request,'brass.html')





