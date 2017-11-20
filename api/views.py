from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PacienteSerializer, PostoSerializer, SubjetivaSerializer
from .models import Paciente, Posto, Subjetiva
from .permissions import IsOwner

# Chamadas Paciente
class CreatePaciente(generics.ListCreateAPIView):
	queryset = Paciente.objects.all()
	serializer_class = PacienteSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwner)

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)

class DetailsPaciente(generics.RetrieveUpdateDestroyAPIView):
	queryset = Paciente.objects.all()
	serializer_class = PacienteSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwner)

# Chamadas Posto
class CreatePosto(generics.ListCreateAPIView):
	queryset = Posto.objects.all()
	serializer_class = PostoSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)

class DetailsPosto(generics.RetrieveUpdateDestroyAPIView):
	queryset = Posto.objects.all()
	serializer_class = PostoSerializer
	permission_classes = (permissions.IsAuthenticated,)


# Chamadas Análise Subjetiva
class CreateSubjetiva(generics.ListCreateAPIView):
	queryset = Posto.objects.all()
	serializer_class = SubjetivaSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)

class DetailsSubjetiva(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subjetiva.objects.all()
	serializer_class = PacienteSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwner)