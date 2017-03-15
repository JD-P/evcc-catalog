from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings


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
        outrows = []
        for result in results:
            # Temporarily just title + course_id for now,
            # will eventually include more fields.
            outrows.append((result.title, result.course_id))
        return render(request,
                      'results.html',
                      {"outrows":outrows,
                       "class_schedule_url":settings.CLASS_SCHEDULE_URL})
    else:
        return HttpResponse("Use a GET request, silly. :3")
        pass
    return 
