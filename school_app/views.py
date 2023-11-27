from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from school_app import models
from school_app.models import Order


# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("haaaiii")

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('userinfo.html')
        else:
            messages.info(request,"Invalid credentials!")
            return redirect('login')
    return render(request,'login.html')

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
                # return redirect('/')
                # print("user created")
        else:
            messages.info(request, 'Password conform faild!')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

# def buy(request):
#     return redirect('/')
def buy(request):
    if request.method == 'POST':
        name = request.POST['name']
        addr = request.POST['addr']
        dob = request.POST['dob']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        dept = request.POST['dept']
        course = request.POST['course']
        purpose = request.POST['purpose']
        material = request.POST['m1']+ request.POST['m2']+ request.POST['m3']+ request.POST['m4']+ request.POST['m5']+ request.POST['m6']
        user = Order.objects.create(name=name,
                                    addr=addr,
                                    dob=dob,
                                    gender=gender,
                                    phone=phone,
                                    email=email,
                                    dept=dept,
                                    course=course,
                                    purpose=purpose,
                                    material=material
                                    )
        user.save();
        #window.alert("Orser")
        return redirect('/')


    return render(request, 'register.html')