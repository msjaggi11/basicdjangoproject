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
    return render(request,"base.html",{"randNum": num})
