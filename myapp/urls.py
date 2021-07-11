from django.urls import path
from django.conf.urls import url
from . import views

app_name = "myapp"

urlpatterns = [
	path("contact/", views.contact, name="contact"),
	path("saisie/", views.saisie, name="saisie"),
	path("httpresponse/", views.http_response_form, name="httpresponse"),
	url(r'^$', views.index, name='index'),
	url(r'^successpage/$', views.successpage, name='successpage'),  
]