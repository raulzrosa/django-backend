from rest_framework import serializers
from .models import Paciente, Posto, Subjetiva


class PacienteSerializer(serializers.ModelSerializer):

	owner = serializers.ReadOnlyField(source = 'owner.username')

	class Meta:
		model = Paciente
		fields = ('id', 'nome', 'nro_sus', 'data_nascimento', 'owner')


class PostoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Posto
		fields = ('id', 'nome', 'bairro')


class SubjetivaSerializer(serializers.ModelSerializer):

	paciente = serializers.ReadOnlyField(source = 'paciente.nome')
	class Meta:
		model = Subjetiva
		fields = ('paciente', 'q1_perdeu_peso')