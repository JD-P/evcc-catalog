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
            instructors = ";".join(join_related(result.instructors_set, "instructor"))
            try:
                requirements = ",".join(join_related(
                    result.requirements_set,
                    "requirement"))
            except TypeError:
                requirements = "N.A"
            conditions = ",".join(join_related(result.conditions_set, "condition"))
            outrows.append((result.course_id,
                            result.title,
                            instructors,
                            requirements,
                            conditions,
                            result.section,
                            result.credits,
                            result.capacity,
                            result.enrolled,
                            result.location,
                            result.start_end))
        return render(request,
                      'results.html',
                      {"outrows":outrows,
                       "class_schedule_url":settings.CLASS_SCHEDULE_URL})
    else:
        return HttpResponse("Use a GET request, silly. :3")
        pass
    return 

def legend(request):
    if request.method == 'GET':
        return render(request,
                      'legend.html',
                      {})
    else:
        return HttpResponse("Use a GET request, silly. :3")

def join_related(related_set, attribute):
    """Join related models which may have multiple elements into a single string 
    for output."""
    items_formatted = []
    for item in related_set.all():
        items_formatted.append(getattr(item, attribute))
    return items_formatted
