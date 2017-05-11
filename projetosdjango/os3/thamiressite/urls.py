from django.conf.urls import url
from thamiressite import views


urlpatterns = [
	url(r'^$', views.principal),
]