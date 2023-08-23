from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index_view(request):
    context = {
        'title': 'Çalışma Alanı',
    }
    return render(request, 'theme/index.html', context)
