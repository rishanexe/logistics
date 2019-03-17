from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
   return render(request, 'logsapp/home.html')

@login_required
def customer(request):
   return render(request, 'logsapp/customer.html')

def deliveryform(request):
   return render(request, 'logsapp/deliveryform.html')