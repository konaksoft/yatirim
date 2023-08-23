from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from apps.accounts.models import User


def login_view(request):
    context = {
        'title': 'Login',
    }
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_info = authenticate(username=username, password=password)
        if user_info:
            login(request, user_info)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username and/or password are incorrect')
            return redirect('login')
    else:
        return render(request, 'management/accounts/login.html', context)


@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required()
def profile_view(request):

    context = {
        'title': 'Profilim',
    }

    if request.POST:
        id = request.user.id
        print(id)
        record = User.objects.get(id=id, is_deleted=False)

        record.first_name = request.POST.get("first_name")
        record.last_name = request.POST.get("last_name")
        record.job_title = request.POST.get("job_title")
        record.email = request.POST.get("email")
        record.mobile_phone = request.POST.get("phone")

        password = request.POST.get("password")
        if len(password) > 0:
            record.set_password(request.POST.get("password"))

        if 'avatar' in request.FILES:
            record.avatar = request.FILES['avatar'] if 'avatar' in request.FILES else False

        try:
            record.save()
            context["status"] = "success"
            context["status_message"] = "Record successfully added"
        except Exception as e:
            context["status"] = "danger"
            context["status_message"] = "An error occurred"

    return render(request, 'management/accounts/profile.html', context)

