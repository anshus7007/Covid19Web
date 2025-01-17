import requests
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    data =True
    result=None
    globalSummary=None
    countries=None
    while(data):
        try:
            result=requests.get("https://api.covid19api.com/summary")
            globalSummary=result.json()['Global']
            countries=result.json()['Countries']
            data=False
        except:
            data=True
    return render(request,'index.html',{'globalSummary':globalSummary,'countries':countries})