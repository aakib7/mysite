from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import RigisterForm



# Create your views here.
def register(request):
    if request.method == "POST":
        form = RigisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {user_name},your account is created successfuly')
            return redirect ('login')
    else:
        form = RigisterForm()
    return render(request,'users/register.html',{
        'form' : form })
 
 
@login_required   
def profile_page(request):
    return render(request,'users/profile.html')
