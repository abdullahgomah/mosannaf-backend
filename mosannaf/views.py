from django.shortcuts import render
from django.contrib import messages
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
    search_input = request.GET['search_input'] 
    if search_input != "":
        # show message here
        results = Mosannaf.objects.filter(name__contains=search_input)
        
    else:
        messages.add_message(request, messages.ERROR,'الحقل فارغ! الرجاء كتابة كلمة البحث ')
        results = "" 
    
    context = {
        'results': results,
        'search_word': request.GET['search_input'],
    } 

    return render(request, 'mosannaf/search_results.html', context)

