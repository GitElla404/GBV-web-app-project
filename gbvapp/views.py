from django.http import HttpResponse
from django import *
from django.shortcuts import render, redirect
from .forms import EmailForm
from .models import Email
from django.contrib import messages

# Create your views here.

def collect_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_entry = Email(email=email)
            email_entry.save()
            
            messages.success(request, "Your email has been added.")
            return redirect('homepage') 
    else:
        form = EmailForm()
    
    return render(request, 'email_collection.html', {'form': form})

def homepage(request):
    active_page = 'homepage'
    return render(request, 'index.html', {'active_page': active_page})

def reportincident(request):
    active_page = 'reportincident'
    return render(request, 'reportincident.html', {'active_page': active_page})

def supportservices(request):
    active_page = 'supportservices'
    return render(request, 'supportservices.html', {'active_page': active_page})


def aboutus(request):
    active_page = 'aboutus'
    return render(request, 'aboutus.html', {'active_page': active_page})




def custom_404(request, exception):
    return render(request, '404.html', status=404)
