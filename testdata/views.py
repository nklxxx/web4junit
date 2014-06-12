from django.shortcuts import render
from django.http import HttpResponse
from models import Data

# Create your views here.

def index(request):
	return HttpResponse('hello world')

def page(request, path):
	return HttpResponse(path)

def table(request, path, name):
	obj = Data.objects.get(path=path, name=name)
	context = { 'data': obj.data }
	return render(request, 'testdata/table.html', context)
