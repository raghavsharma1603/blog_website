from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    # return HttpResponse("Education for Nation")
    return render(request,'home.html')

