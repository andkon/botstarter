from django.conf.urls import patterns, url
from .views import *

urlpatterns = [
	url(r'^sms/$', SMSView.as_view()),
]