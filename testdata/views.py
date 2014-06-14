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

def save(request):
	path = request.POST["path"]
	name = request.POST["name"]
	data = request.POST["data"]
	#data = request.raw_post_data
	obj = Data.objects.get(path=path, name=name)
	obj.data = data
	obj.save()
	return HttpResponse('ok')

def get(request):
	path = request.GET["path"]
	name = request.GET["name"]
	obj = Data.objects.get(path=path, name=name)
	data = obj.data
	return HttpResponse(data)
