from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)

class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    capacidade = models.IntegerField()

class Reserva(models.Model):
    data_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)