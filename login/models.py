from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import tree
# Create your models here.



class Senha(models.Model):
    nome = models.CharField(max_length=200)
    senha = models.PositiveIntegerField(blank=False,default=0)
    Representacao = models.CharField(verbose_name="Representação",max_length=100)
    parque = models.ForeignKey("parque", on_delete=models.CASCADE, related_name='Senha',null=True,blank=True)
    def __str__(self) -> str:
        return self.nome


    

class Parque(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.CharField(verbose_name="Cidade",max_length=100)
    estado = models.CharField(verbose_name="Estado",max_length=100)

    def __str__(self) -> str:
        return self.nome   


class User(AbstractUser):
    bio = models.TextField(blank=True,max_length=100)
    # parque = models.ManyToManyField('parque',on_delete=models.SET_NULL, null=True,related_name='usuario')
    parque = models.ForeignKey("parque", on_delete=models.CASCADE, related_name='usuario',null=True,blank=True)

    
