from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Successful.')
            return redirect('register')
    else: 
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request,'account/register.html',context)

@csrf_exempt
def my_view(request):
   return render(request,'account/login.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            # messages.success(request, "You are now logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
            # auth.login(request,user)
            # messages.success(request, "You are now logged in.")
            # return redirect('home')
    return render(request,'account/login.html')

def logout(request):
    return render(request,'account/logout.html')