from django.shortcuts import render
from django.http import HttpResponse
from models import Data

# Create your views here.

def index(request):
	objs = Data.objects.all()
	list_path = set(obj.path for obj in objs)
	context = { 'list_path': list_path}
	return render(request, 'testdata/index.html', context)

def page(request, path):
	objs = Data.objects.filter(path=path)
	context = { 'objs': objs }
	return render(request, 'testdata/table.html', context)
