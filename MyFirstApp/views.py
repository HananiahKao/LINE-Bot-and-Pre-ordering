from django.http import HttpResponse
from urllib.parse import unquote
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
import os
from requests import get
from DatabaseManager import DBManager

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
    get('https://mysite-6c9q.onrender.com')
    print("I'm still alive!")
    return HttpResponse("I'm still alive!")

def runShell(request):
    try:
        manager = DBManager()
        command = request.GET.get('command', '')

        # Run the Shell script command
        process = subprocess.Popen(command.strip(), shell=True, cwd=manager.read_value('cwd',os.path.expanduser("~")), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if command.startswith("cd"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                target_dir = parts[1]
            else:
                target_dir = os.path.expanduser("~") # Default to home directory

            # Resolve new directory
            new_cwd = os.path.abspath(os.path.join(manager.read_value('cwd',os.path.expanduser("~")), target_dir))
            if os.path.exists(new_cwd.replace('\\ ',' ')):
                manager.write_value('cwd',new_cwd.replace('\\ ',' '))

            # Return the output and errors
        def checkOutput():
            # Yield each line of stdout as it becomes available
            while True:
            # Capture any errors
                output = process.stdout.readline()
                if output:
                    yield f"data: {output}\n\n"
                stderr = process.stderr.read()
                if stderr and output == '':
                    yield f"data: Error: {stderr}\n\n"
                if output == '' and process.poll() is not None:
                    yield "data: Process-ended\n\n"
                    break

        return HttpResponse(checkOutput(), content_type='text/event-stream')
    except Exception as e:
        def error_event():
            yield f"data: Error: {str(e)}\n\n"
        return HttpResponse(error_event(), content_type='text/event-stream')

    
def shellPage(request):
    return render(request, "runShellScript.html")
