from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic_modelform(request):
    TMFO=ModelTopicForm()
    d={'form':TMFO}
    if request.method=="POST":
        FD=ModelTopicForm(request.POST)
        if FD.is_valid():
            FD.save()
        return HttpResponse('topic_is inserted succssfully by using modelforms')
    return render(request,'topic_modelform.html',d)

def webpage_modelform(request):
    WMFO=ModelWebpageForm()
    d={'form':WMFO}
    if request.method=="POST":
        FD=ModelWebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
        return HttpResponse('webpage_is inserted succssfully by using modelforms')
    return render(request,'webpage_modelform.html',d)

def accessrecords_modelform(request):
    AMFO=ModelAccessRecordsForm()
    d={'form':AMFO}
    if request.method=="POST":
        FD=ModelAccessRecordsForm(request.POST)
        if FD.is_valid():
            FD.save()
        return HttpResponse('webpage_is inserted succssfully by using modelforms')
    return render(request,'accessrecords_modelform.html',d)