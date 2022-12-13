from django.shortcuts import render
from .models import *

# Create your views here.


def all(request):
    mosannafs = Mosannaf.objects.all().order_by('-date_published')

    context ={
        'mosannafs': mosannafs, 
    } 

    return render(request, 'mosannaf/all.html', context)
    


def details(request, id):
    mosannaf = Mosannaf.objects.get(id=id)
    rates = Rate.objects.filter(mosannaf=mosannaf) 

    context = {
        'mosannaf': mosannaf,
        'rates': rates, 
    }

    return render(request, 'mosannaf/mosannaf_details.html', context)


def search(request): 
    
    results = Mosannaf.objects.filter(name__contains=request.GET['search_input'])
    
    context = {
        'results': results,
        'search_word': request.GET['search_input'],
    } 

    return render(request, 'mosannaf/search_results.html', context)