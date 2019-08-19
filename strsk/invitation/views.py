from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Birthday
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,ProfileForm,BirthdayForm


def home(request):
    return render(request, 'base.html')

def bday(request):
    return render(request, 'users/bday.html')

def def_wish(request):
    return render(request, 'users/dif_wish.html')

def birthday(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            y=form.cleaned_data['queen']
            a=form.cleaned_data['image']
            #form.save(commit=True)
            try:
                Birthday.objects.create(user=request.user,queen=y,image=a)
                messages.success(request, f'Your Wish has been created!')
                return redirect('bday')

            except:
                messages.warning(request, f'Already you have done! update that')
                return redirect('profile')
            

    else:
        form = BirthdayForm()
        
    context = {
        'form': form
    }

    return render(request, 'users/birthday.html', context)

def wish(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            x=form.cleaned_data['king']
            y=form.cleaned_data['queen']
            a=form.cleaned_data['image']
            b=form.cleaned_data['image1']
            #form.save(commit=True)
            try:
                Profile.objects.create(user=request.user,king=x,queen=y,image=a,image1=b)
                messages.success(request, f'Your account has been updated!')
                return redirect('home')

            except:
                messages.warning(request, f'Already you have wished! update that')
                return redirect('profile')
            

    else:
        form = ProfileForm()
        
    context = {
        'form': form
    }

    return render(request, 'users/wish.html', context)

    
@login_required
def home1(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        #u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            #u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        #u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        #'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)