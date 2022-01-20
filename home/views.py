from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'ABOUT.html')
def services(request):
    return render(request, 'SERVICES.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone = request.POST.get('Phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,Phone=Phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'CONTACT.html')
def orders(request):
    return render(request, 'ORDERS.html')



