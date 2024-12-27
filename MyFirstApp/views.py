from django.http import HttpResponse
from urllib.parse import unquote
from django.shortcuts import render


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
