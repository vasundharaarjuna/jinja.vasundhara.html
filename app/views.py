from django.shortcuts import render

# Create your views here.
def jinja(request):
    d=context={'name':'Ashu','age':20}
    return render(request,'jinja.html',d)