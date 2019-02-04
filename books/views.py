#import responder.status_codes as status_codes
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("[{\"msg\": \"Hello World!\"}]")

