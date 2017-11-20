from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreatePaciente, DetailsPaciente
from .views import CreatePosto, DetailsPosto
from .views import CreateSubjetiva, DetailsSubjetiva


urlpatterns = {	

	# Paciente
	url(r'^pacientes/$', CreatePaciente.as_view(), name = 'create'),
	url(r'^paciente/(?P<pk>[0-9]+)/$', 
	DetailsPaciente.as_view(), name = "details"),

	# Posto
	url(r'^postos/$', CreatePosto.as_view(), name = 'create'),
	url(r'^posto/(?P<pk>[0-9]+)/$', 
	DetailsPosto.as_view(), name = "details"),

	# Avaliação Subjetiva
	url(r'^subjetiva/$', CreateSubjetiva.as_view(), name = 'create'),
	url(r'^paciente/(?P<pk>[0-9]+)/subjetiva/$', 
	DetailsSubjetiva.as_view(), name = "details"),

	url(r'^auth/', include('rest_framework.urls', 
                               namespace = 'rest_framework')), 
}

urlpatterns = format_suffix_patterns(urlpatterns)

