from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import send_mail as Send_Mail
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from apps.forms.models import *


def add_form(request):
    context = {
        'title': 'Form Ekle',
    }
    if request.POST:

        new_record = Forms()
        new_record.step1 = request.POST.get('step1')
        new_record.step2 = request.POST.get('step2')
        new_record.step3 = request.POST.get('step3')
        new_record.step4 = request.POST.get('step4')
        new_record.phone = request.POST.get('phone')
        new_record.email = request.POST.get('email')
        new_record.name = request.POST.get('name')
        gender = request.POST.get('gender')
        if gender =='Erkek':
            new_record.gender = 0
        else:
            new_record.gender = 1
        new_record.created_on = timezone.now()
        try:
            new_record.save()
            return JsonResponse({'result': True})
        except Exception as e:
            return JsonResponse({'error': True, 'error_msg': str(e)})
    else:
        return render(request, 'theme/index.html', context)


@login_required()
def delete_form(request):
    record_id = request.POST.get('id')
    try:
        record = Forms.objects.get(id=record_id)
        record.is_deleted = True
        record.save()
        return JsonResponse({'result': True})
    except Exception as e:
        return JsonResponse({'error': True, 'error_msg': str(e)})
