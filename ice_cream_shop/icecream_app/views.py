import json
from pdb import post_mortem
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def home(request):
    page_name='Home'
    username=request.session['username']
    context={'page_name':page_name,
            'username':username}
    return render(request,'home_page.html',context)
    
def about(request):
    page_name='About'
    username=request.session['username']
    context={'page_name':page_name,
            'username':username}
    return render(request,'about.html',context)

def product(request):
    page_name='Product' 
    username=request.session['username']
    context={'page_name':page_name,
            'username':username}
    return render(request,'product.html',context)    

def service(request):
    page_name='Service'
    username=request.session['username']
    context={'page_name':page_name,
            'username':username}
    return render(request,'service.html',context)  

def gallery(request):
    page_name='Gallery'
    username=request.session['username']
    context={'page_name':page_name,
            'username':username}
    return render(request,'gallery.html',context)  

def contact(request): 
    page_name='Orders'
    username=request.session['username']
    messsage='You are not choosed any items go to product page and purchase something'
    context={'page_name':page_name,
            'username':username,
            'message':messsage}
    return render(request,'contact.html',context)     

def contact_submit(request):
    name = request.POST['name']
    email =request.POST['email']
    subject =request.POST['subject']
    message =request.POST['message']
    print(name,email,subject,message)
    return render(request,'contact.html')     

def order_details(request):
    cart_data = request.GET.get('cart_data')
    username=request.session['username']
    page_name='Orders'
    js_data = json.loads(cart_data)
    
    if cart_data is not None:
        ice_name=[i['name'] for i in js_data]
        ice_price=[i['price'] for i in js_data]
        ice_count=[i['count'] for i in js_data]
        ice_total=[i['total'] for i in js_data]
        # Convert the string values to floats
        ice_total = [float(value) for value in ice_total]

        # Optionally, round the float values to integers
        ice_total = [int(round(value)) for value in ice_total]

        total_sum = sum(ice_total)
        ice_data = zip(ice_name, ice_price, ice_count, ice_total)
        

        context={
            "ice_data":ice_data,
            'username':username,
            "total_sum":total_sum,
            "page_name":page_name
        }
        
             

    return render(request, 'contact.html',context)
     
    