from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard:dashboard'))
    else:
        return render(request, 'login/login.html')


def logging_in(request):
    if request.method == 'POST':
        print('wew1')
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        request.session['username'] = username
        if user is not None:
            login(request, user)
            if auth.is_superuser:
                return render(request, 'dashboard/index.html')
        else:
            return render(request, 'login/login.html', {})
    else:
        return HttpResponseRedirect(reverse('dashboard:index'))


def dashboard(request):
    return render(request, 'dashboard/index.html')

def logging_out(request):
    del request.session['username']
    logout(request)
    return HttpResponseRedirect(reverse('dashboard:index'))
