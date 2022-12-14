from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import * 
from django.http import JsonResponse
from django.core import serializers

# Create your views here.


def all(request):
    mosannafs = Mosannaf.objects.all().order_by('-date_published')

    context ={
        'mosannafs': mosannafs, 
    } 

    return render(request, 'mosannaf/all.html', context)
    


def details(request, id):
    mosannaf = Mosannaf.objects.get(id=id)
    form = RateForm() 
    rates = Rate.objects.filter(mosannaf=mosannaf) 
    
    context = {
        'mosannaf': mosannaf,
        'rates': rates, 
        'form': form, 
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




def add_rate(request):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = RateForm(request.POST)
        
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)