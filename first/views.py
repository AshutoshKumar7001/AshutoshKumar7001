from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Demo message from views')

def page1(request):
    return HttpResponse('Redirecting to the first page inside the demo views.')
