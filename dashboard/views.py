from django.shortcuts import render
from mosannaf.models import Mosannaf

# Create your views here.
def dashboard(request):
    context ={}
    return render(request, 'dashboard/index.html', context)


def get_last_five_mosannaf(request):
    results = Mosannaf.objects.all()[:5]
    context = {
        'results': results,
    }
    return render(request, 'dashboard/lastfive.html', context)