from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    return render(request, 'index.html')


class index2(TemplateView):
    template_name = 'index2.html'

class index3(TemplateView):
    template_name = 'index3.html'

class index4(TemplateView):
    template_name = 'index4.html'
