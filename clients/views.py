from django.shortcuts import render
from .forms import RequestForm

def index(request):
    error = ''
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Error'



    date = {
        'form': form,
        'error' : error
    }

    return render(request, 'clients/index.html', date)
