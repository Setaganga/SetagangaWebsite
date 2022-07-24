from django.http import HttpResponse
from django.template import loader

def index(request):
    htmlpage = loader.get_template('Home.html')
    return HttpResponse(htmlpage.render())

def login(request):
    htmlpage = loader.get_template('login.html')
    return HttpResponse(htmlpage.render())

def aboutme(request):
    htmlpage = loader.get_template('aboutme.html')
    return HttpResponse(htmlpage.render())
