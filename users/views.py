from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

#회원가입
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login') #회원 가입 후 로그인 화면으로
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

#로그인 기능
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users/home.html')#로그인 성공시
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

#로그아웃 기능
def user_logout(request):
    logout(request)
    return redirect('users/home.html')
