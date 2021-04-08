from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from .forms import NewUserForm

def register(request):
    if request.method != 'POST':
        form = NewUserForm()
    else:
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('foddys:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_request(request):
    logout(request)
    return redirect('foddys:index')

def login_request(request):
    # if request.method != 'POST':
    #     form =AuthenticationForm()
    # else:
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('foddys:index')
            else:
                messages.error(request, 'Niepoprawny login lub hasło')
        else:
            messages.error(request, 'Niepoprawny login lub hasło')

    form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})