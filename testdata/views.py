from django.shortcuts import render
from django.http import HttpResponse
from models import Data

# Create your views here.

def index(request):
	return HttpResponse('hello world')

def page(request, path):
	objs = Data.objects.filter(path=path)
	context = { 'objs': objs }
	return render(request, 'testdata/table.html', context)
