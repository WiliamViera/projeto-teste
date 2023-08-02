from django.db import models

class estados(models.Model):
    EstadoID = models.AutoField(primary_key=True)
    Estado = models.TextField(max_length=255)
    TotalPesq = models.IntegerField(default=0)
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'Estados'

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    estado = models.TextField(max_length=255)

    class Meta:
        db_table = 'Usuario'

