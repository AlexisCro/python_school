from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  return HttpResponse()

