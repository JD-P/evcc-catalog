from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^courses/$', views.search_results),
    url(r'^$', views.simple_search_view, name="index"),
]
