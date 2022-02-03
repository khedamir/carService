from django.shortcuts import render

# Create your views here.

from main.models import repairRequest
from django.shortcuts import redirect


def index(request):
    status_q = request.GET.get("status")
    if not status_q:
        rRequest = []
    else:
        rRequest = repairRequest.objects.filter(status=status_q)

    if request.user.groups.filter(name = "service").exists():
        return render(request, 'service/index.html', {'rRequest': rRequest})
    else: 
        return redirect('login')


def changeStatusMan(request):
    a=request.GET.get('id')
    b=request.GET.get('status')
    repairRequest.objects.filter(id=a).update(status='2')
    return redirect('main')