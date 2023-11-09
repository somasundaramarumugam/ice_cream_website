from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.
def index(request):
    return render(request,'login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    request.session['username']=username
    # try:
    if User.objects.filter(username=username).exists():
        page_name='Home'
        context={
            'page_name':page_name,
            'username':username
        }
        return render(request,'home_page.html',context)
# except:
    else:
        message='User Does Not Exist'
        context={
            'message':message
        }
        return render(request,'login.html',context)


def signup(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    mobile_no=request.POST['mobile_no']

    user_details=User.objects.create(username=username, email=email, password=password)
    usr = UserProfile(user=user_details,mobile_number=mobile_no)
    usr.save()
    
    status='hide'
    context={
        'status':status
    }
    return render(request,'login.html',context)