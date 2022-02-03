from django.shortcuts import render

# Create your views here.

from main.models import repairRequest
from django.shortcuts import redirect


def index(request):
    status_q = request.GET.get("status")
    if not status_q:
        rRequest = repairRequest.objects.filter(status='1')
    else:
        rRequest = repairRequest.objects.filter(status=status_q)

    if request.user.groups.filter(name = "service").exists():
        return render(request, 'service/index.html', {'rRequest': rRequest})
    else: 
        return redirect('login')


def changeStatusMan(request):
    a=request.GET.get('id')
    rStatus = request.GET.get('status')
    rRequest = repairRequest.objects.get(id=a)

    if rStatus == '1':
        rRequest.status = 2
        rRequest.save()
    elif rStatus == '2':
        rRequest.status = 3
        rRequest.save()
    else:
        rRequest.delete()
    
    return redirect('service')