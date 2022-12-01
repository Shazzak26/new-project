from django.shortcuts import render

from django.http import HttpResponse

from .forms import UserRegistrationForm

def account(request):
    return render(request, 'administrator/base.html')


def register(request):
    
    if request.method == 'POST':
        data = request.POST
        form = UserRegistrationForm(data)
        if form.is_valid():
            form.save()
    context = {'form': UserRegistrationForm()}
    return render(request, 'user/register.html', context)
