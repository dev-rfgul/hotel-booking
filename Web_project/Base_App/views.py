from django.shortcuts import render, redirect
from django.http import HttpResponse
from Base_App.models import BookTable, AboutUs, Feedback,ItemList, Items
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def Signup_View(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if user.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
        else:
            user = user.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=name
            )
            user.save()
            # Optional: Save phone somewhere if using a profile model
            login(request, user)
            return redirect('home')  # Redirect to your homepage
    return render(request, 'signup.html')


def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request,'home.html',  {'items': items, 'list' : list, 'review' : review})

def AboutView(request):
    return render(request,'about.html')

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request,'menu.html', {'items': items, 'list' : list})

def BookTableView(request):
    if request.method =='POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        user_email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')
        if name and user_email and total_person and booking_data:
            data = BookTable(
                Name=name,
                Phone_number=phone_number,
                Email=user_email,
                Total_person=total_person,
                Booking_data=booking_data
            )
            data.save()
              
    return render(request,'book_table.html')

def FeedbackView(request):
    return render(request,'feedback.html')