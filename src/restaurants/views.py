from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # html_var = "Hello World from f strings."    
    # html_ =f'''
    #     <html>
    #     <body>
    #     <h1> {html_var.upper()} </h1>
    #     </body>
    #     </html>
    # '''
    # return HttpResponse(html_)
    num = random.randint(0,1000000)
    params = {
        "num" : num,
        "items": [num, random.randint(0,1000000)],
        "bool_item": True
        }
    return render(request,"home.html",params)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")    
