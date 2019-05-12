from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html_var = "Hello World from f strings."    
    html_ =f'''
        <html>
        <body>
        <h1> {html_var.upper()} </h1>
        </body>
        </html>
    '''
    return HttpResponse(html_)
