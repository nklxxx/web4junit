from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
	return HttpResponseRedirect("/testdata/") 
