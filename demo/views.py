from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.

class Another(View):

    books = Book.objects.all()

    # output = f"We have {len(book)} that many books in DB."
    output = ''

    for book in books:
        output += f"We have {book.title} that many books in DB.<br>"

    def get(self, request):
        return HttpResponse(self.output)


    # def get(self, request):
    #     return HttpResponse('This is the insideclass funtion inside the class demo.')


def home(request):
    return HttpResponse('First message from views')

def page1(request):
    return HttpResponse('Redirecting to the first page.')
