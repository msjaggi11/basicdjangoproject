from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views import View 
from django.views.generic import TemplateView

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


#see below for new implementation using TemplateView class.
# def about(request):
#     return render(request,"about.html")

# def contact(request):
#     return render(request,"contact.html")    

#implement get method inside Class Based Views.
class ContactView(View):
    def get(self,request,*args,**kwargs):
        key = 'id'
        if key not in kwargs:
            kwargs[key]=None
        return render(request,"contact.html",{'id':kwargs[key]})


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
    def get_context_data(self,*args,**kwargs):
        context = super(ContactTemplateView,self).get_context_data(*args,**kwargs)
        context = {'id': random.randint(0,10)}
        return context

class AboutTemplateView(TemplateView):
    template_name = 'about.html'


