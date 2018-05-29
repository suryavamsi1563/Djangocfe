import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# def home(rquest):
#     html_var = "f strings"
#     html_1 = f"""
#     <!DOCTYPE html>
#     <html lang=en>
#     <head>
#     </head>
#     <body>
#     <h1>Hello World</h1>
#     <p>This is a {html_var} page</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_1)
# Create your views here.

def home(request):
    num = random.randint(0,100000000)
    some_list = [num,
    random.randint(0,100000000),
    random.randint(0,100000000),
    random.randint(0,100000000)
    ]
    context = {
        "html_var":"context_variables",
        "num":num,
        "sample_list":some_list,
        "hai":True
    }
    return render(request,"home.html",context)

def home2(request):
    context = {

    }
    return render(request,"home2.html",context)

def home3(request):
    context = {

    }
    return render(request,"home3.html",context)

class ContactView(View):
    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,"contact.html",context)
