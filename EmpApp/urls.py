from django.conf.urls import url
from EmpApp import views

urlpatterns = [
    url(r'^emp/$', views.EmpView.as_view()),
    url(r'^emp/(?P<pk>[0-9]+)',views.EmpDetails.as_view()),

]





