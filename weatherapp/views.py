from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    text = request.GET['words']
    num_words = len(text.split())
    return render(request, 'result.html', {'num': num_words})