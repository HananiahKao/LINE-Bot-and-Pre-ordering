from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def HomePage(request):
    viewerName="Hananiah"
    response = render(request, "HomePage.html", locals())
    return response
def liffPage(request):
    selected = request.GET.get('selected','')
    response = render(request, "liff.html", locals())
    return response
