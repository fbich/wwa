from django.urls import path

from django.conf.urls import url
from . import views

app_name = "myapp"

urlpatterns = [
	url("contact", views.contact, name="contact"),
	path("saisie", views.saisie, name="saisie"),
	url("grille", views.grille, name="grillen"),
	url("page2", views.page2, name="webpage2"),
	url("page3", views.page3, name="webpage3"),
	url("home", views.home, name="webhome"),
	path("httpresponse/", views.http_response_form, name="httpresponse"),
	url(r'^$', views.index, name="index"),
	url(r'^successpage/$', views.successpage, name='successpage'),  
]