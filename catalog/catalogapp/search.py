from catalogapp.models import *
from django.db.models import Q

def simple_search_query(qstring):
    # Search title, description, instructors, location
    if qstring.get("multisearch"):
        search_parameter = qstring.get("multisearch")
        courses_query = (Q(title__icontains=search_parameter) |
                         Q(description__icontains=search_parameter) |
                         Q(location__icontains=search_parameter))
        courses = Course.objects
        ms_courses_results = courses.filter(courses_query)
        instructors = Instructors.objects
        instructors = instructors.filter(instructor__icontains=search_parameter)

    # Handle search by day
        
    day_filters = [(value, qstring.get(value)) for value in ("monday",
                                                              "tuesday",
                                                              "wednesday",
                                                              "thursday",
                                                              "friday")]
    days_conv = {"monday":"M",
                 "tuesday":"T",
                 "wednesday":"W",
                 "thursday":"Th",
                 "friday":"F",
                 "saturday":"Sa",
                 "sunday":"Su"}
    days = Days.objects
    for day_filter in day_filters:
        if day_filter[1]:
            day_string = days_conv[day_filter[0]]
            days.filter(day__iexact=day_string)

    # Look at conditions
    cond_filters = [(value, qstring.get(value)) for value in ("annual",
                                                              "ec",
                                                              "hybrid",
                                                              "honors",
                                                              "lc",
                                                              "online",
                                                              "web_enhanced")]
    cond_conv = {"annual":"A",
                 "ec":"EC",
                 "hybrid":"H",
                 "honors":"HN",
                 "lc":"LC",
                 "online":"OL",
                 "web_enhanced":"WE"}
    conditions = Conditions.objects
    for cond_filter in cond_filters:
        if cond_filter[1]:
            cond_string = cond_conv[cond_filter[0]]
            conditions.filter(condition__iexact=cond_string)
