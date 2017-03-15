from django.shortcuts import render

from . import forms

# Create your views here.

def simple_search_view(request):
    return render(request,
                  'search.html',
                  {'form':forms.SimpleSearchForm()})
