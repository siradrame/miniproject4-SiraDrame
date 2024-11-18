# INF601 - Advanced Programming in Python
# Sira  Drame
# Mini Project 4

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import ContactForm  # Custom form for contact page

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
