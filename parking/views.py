from django.shortcuts import render,redirect
from django.conf.urls import url
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from parking import models
from parking.models import Park,Book

# from parking.models import Park
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password) 

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            print("Invalid credentials")
            messages.info(request,"Invalid credentials")
            return redirect('login')

    else:
        return render(request,"login.html")
    

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['mobile_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        #last_name=first_name.split(' ')[1]
        if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Mobile number taken")
                    print('Username taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    messages.info(request,"User created")
                    print('User created')
                    return redirect('login')
        else:
            messages.info(request,"password not matching!!")
            return redirect('register')
        
    else:
        return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('home')	

def profile(request):
    return render(request,'profile.html')

def creatparkingslot(request):
    if request.method =="POST":
        parkid =request.POST['park_id']
        park_name =request.POST['park_name']
        date = request .POST['date']
        park_location = request .POST['park_location']
        slot_type = request .POST['slot_type']
        slotsNo = request .POST['slots']
        
        wuser=Park.objects.create(parkid=parkid,park_name=park_name,date=date,park_location=park_location,slot_type=slot_type,slotsNo=slotsNo)
        wuser.save()
        messages.info(request,' Parking slot is Created ')
        return redirect('creatparkingslot')
    else:
        supers = Park.objects.all()
        context = {'x': supers}    

    return render(request,'creatparkingslot.html',context)

def evcharging(request):
    supers = Park.objects.filter(slot_type="EV-Charging")
    return render(request,'evcharging.html',{'supers':supers})

def parking(request):
    supers = Park.objects.filter(slot_type="Parking") #Parking
    return render(request,'parking.html',{'supers':supers})

def base(request):
    return render(request,'base.html')    

def checkout(request):
    if request.method == 'POST':
        h1= request.POST['slothidden']
        supers = Park.objects.filter(slot_type=h1)
        dict={}
        for u in supers:
            dict["park_name"]=u.park_name,
            dict["park_location"]=u.park_location,
            dict["slot_type"]=u.slot_type,   
        request.session['data']=dict   
    return render(request,'checkout.html',{'x':supers})            

def bookingSuccess(request):
    if request.method == 'POST':
        user_id= request.POST['user']
        user=User.objects.filter(id=user_id)
        vehicle_no = request.POST['vehicle_no']
        start_time = request.POST['start_time']
        end_time=start_time
        dict=request.session.get('data')
        park_name=dict["park_name"]
        park_location=dict["park_location"]
        slot_type=dict["slot_type"]
        #print(park_name[0],park_location[0],slot_type[0])
        book=Book.objects.create(vehicle_no=vehicle_no,start_time=start_time,end_time=end_time,park_name=park_name[0],park_location=park_location[0],slot_type=slot_type[0])
        parkid1=Park.objects.filter(park_name=park_name[0],park_location=park_location[0],slot_type=slot_type[0])
        #print("------------------------",parkid1)
        for p in parkid1:
            id=p.id
        park = Park.objects.get(id=id)  
        park.slotsNo=park.slotsNo-1
        park.save()
        book.save()
        print("booked successfully")
        bookDetails = Book.objects.filter(vehicle_no="MH12RN1")
        # for u in user:
        #     print("---------------------------------------------------------",u.id,u.first_name)
    return render(request,'success.html',{'x':bookDetails})

def deleterecord(request):
    if request.method=='POST':
        f1=request.POST['hide1']
        f2=request.POST['hide2']
        Park.objects.filter(parkid=f1,slot_type=f2).delete()
    # supers = Park.objects.filter(slot_type="EV-Charging",date ='2022-05-03') #Parking
    supers = Park.objects.all() #Parking
    return render(request,'creatparkingslot.html',{'x':supers})