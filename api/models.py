from django.db import models

# Create your models here.


class Paciente(models.Model):
	nome = models.CharField(max_length=100)
	nro_sus = models.CharField(max_length=15)
	data_nascimento = models.DateField()
	owner = models.ForeignKey('auth.User', related_name = 'pacientes',
	on_delete = models.CASCADE)

	def __str__(self):
		return "{}".format(self.nome)


class Posto(models.Model):
	nome = models.CharField(max_length=100)
	numero = models.IntegerField(blank=True)
	endereco = models.CharField(max_length=100, blank=True)
	bairro = models.CharField(max_length=100, blank=True)
	cep = models.CharField(max_length=8, blank=True)
	telefone = models.CharField(max_length=9, blank=True)
	owner = models.ForeignKey('auth.User', related_name = 'postos',
	on_delete = models.CASCADE)

	def __str__(self):
		return "{}".format(self.nome)

class Subjetiva(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	q1_perdeu_peso = models.IntegerField(blank=True)