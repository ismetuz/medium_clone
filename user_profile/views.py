from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request,f'{ request.user.username } Daha önce login olmuşsunuz.')
        return redirect('home_view')
    context = dict()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if len(username) < 6 or len(password)<6:
            messages.warning(request,'Kullanıcı adı veya parolayı yalış girdiniz. Minimum 6 karakter olmalıdır.')
            return redirect('user_profile:login_view')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,f'{ request.user.username } Login oldun.')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)

def logout_view(request):
    messages.info(request,f'{ request.user.username } Oturumun kapatıldı .')
    logout(request)
    return redirect('home_view')

def register_view(request):
    context = dict()
    if request.method == "POST":
        print(request.POST)
    return render(request, 'user_profile/register.html',context)