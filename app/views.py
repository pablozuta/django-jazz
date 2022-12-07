from app.models import Record
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'app/index.html')

def records(request):
    record = Record.objects.all()
    return render(request, 'app/records.html',
    {'record': record})

def biography(request):
    return render(request, 'app/biography.html')
