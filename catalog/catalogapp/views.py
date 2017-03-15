from django.shortcuts import render
from django.http.response import HttpResponse

from . import forms
from . import search


# Create your views here.

def simple_search_view(request):
    return render(request,
                  'search.html',
                  {'form':forms.SimpleSearchForm()})


def search_results(request):
    if request.method == 'GET':
        results = search.simple_search_query(request.GET)
        # Temporary
        return HttpResponse(results[0].title)    
    else:
        #Figure out later
        pass
    return 
