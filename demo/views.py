from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('First message from views')

def page1(request):
    return HttpResponse('Redirecting to the first page.')
