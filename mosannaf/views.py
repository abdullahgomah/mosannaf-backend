from django.shortcuts import render
from .models import *

# Create your views here.


def details(request, id):
    mosannaf = Mosannaf.objects.get(id=id)

    context = {
        'mosannaf': mosannaf
    }

    return render(request, 'mosannaf/mosannaf_details.html', context)
