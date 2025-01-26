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

@csrf_exempt
def runShell(request):
    if request.method == 'POST':
        manager = DBManager()
        try:
            data = json.loads(request.body)
            command = data.get('command', '')

            # Run the Shell script command
            if command.startswith("cd"):
                parts = command.split(maxsplit=1)
                if len(parts) > 1:
                    target_dir = parts[1]
                else:
                    target_dir = os.path.expanduser("~")  # Default to home directory

                # Resolve new directory
                new_cwd = os.path.abspath(os.path.join(manager.read_value('cwd','~'), target_dir))
                manager.write_value('cwd',new_cwd)
            process = subprocess.run(command, shell=True, cwd=manager.read_value('cwd','~'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Return the output and errors
            return JsonResponse({
                'output': process.stdout.strip(),
                'error': process.stderr.strip()
            })
        except Exception as e:
            return JsonResponse({'output': '', 'error': str(e)})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
def shellPage(request):
    return render(request, "runShellScript.html")
