from catalogapp.models import *
from django.db.models import Q
from django.db.models import Max

def simple_search_query(qstring):
    # Grab only the latest version of the data
    courses_current_date = Course.objects.all().aggregate(Max('course_date'))
    courses = Course.objects.filter(course_date=courses_current_date['course_date__max'])
    
    # Search title, description, instructors, location
    if qstring.get("multisearch"):
        search_parameter = qstring.get("multisearch")
        courses = courses.filter(
            Q(title__icontains=search_parameter) |
            Q(description__icontains=search_parameter) |
            Q(location__icontains=search_parameter) |
            Q(instructors__instructor__icontains=search_parameter))
    else:
        pass

    # Search days indicated by user
        
    days_conv = {"monday":"M",
                 "tuesday":"T",
                 "wednesday":"W",
                 "thursday":"Th",
                 "friday":"F",
                 "saturday":"Sa",
                 "sunday":"Su"}
    days_list = mk_checkbox_search_list(days_conv, qstring)
    if days_list:
        courses = courses.filter(days__day__in=days_list)

    # Search conditions indicated by user
        
    cond_conv = {"annual":"A",
                 "ec":"EC",
                 "hybrid":"H",
                 "honors":"HN",
                 "lc":"LC",
                 "online":"OL",
                 "web_enhanced":"WE"}
    cond_list = mk_checkbox_search_list(cond_conv, qstring)
    if cond_list:
        courses = courses.filter(conditions__condition__in=cond_list)

    # Search credit requirements indicated by user
        
    credit_conv = {"aas":"AAS",
                   "c":"C",
                   "ns":"NS",
                   "h":"H",
                   "hp":"HP",
                   "ss":"SS",
                   "ns_l":"NS-L",
                   "q":"Q",
                   "te":"TE",
                   "d":"D"}
    credit_list = mk_checkbox_search_list(credit_conv, qstring)
    if credit_list:
        courses = courses.filter(requirements__requirement__in=credit_list)

    return courses
        
def mk_checkbox_search_list(checkbox_conv_dict, qstring):
    """Make a list of values which have been indicated to search for in a set of
    checkboxes."""
    checkbox_names = list(checkbox_conv_dict.keys())
    check_filters = [(value, qstring.get(value)) for value in checkbox_names]
    search_list = []
    for check_filter in check_filters:
        if check_filter[1]:
            search_list.append(checkbox_conv_dict[check_filter[0]])
    return search_list

