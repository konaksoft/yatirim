from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.accounts.models import User





@login_required()
def dashboard_view(request):
    users = User.objects.filter(is_deleted=False)

    context = {
        'title': 'Çalışma Alanı',
        "users":users
    }

    return render(request, 'management/dashboard/dashboard.html', context)
