from django.shortcuts import render

def login_view(request):
    # Eğer kullanıcı zaten login olduysa anasayfaya gödner
    context = dict()
    return render(request, 'user_profile/login.html', context)
