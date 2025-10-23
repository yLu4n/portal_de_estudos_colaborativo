from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(
        max_length=200,
        unique=True,
        help_text="Nome da disciplina (ex: Matemática, História, etc.)"
    )
    
    descricao = models.TextField(
        blank=True,
        null=True,
        help_text="Descrição detalhada da disciplina"
    )
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Disciplinas"
        ordering = ['nome']

class Material(models.Model):
    titulo = models.CharField(
        max_length=255,
        help_text="Título do material de estudo"
    )
    
    descricao = models.TextField(
        blank=True,
        null=True
    )
    
    arquivo = models.FileField(
        upload_to='materiais/',
        help_text="Selecione o arquivo para upload"
    )
    
    data_upload = models.DateTimeField(
        auto_now_add=True
    )
    
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='materiais_enviados'
    )
    
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='materiais'
    )
    
    def __str__(self):
        return f"{self.titulo}({self.disciplina.nome})"
    
    class Meta:
        verbose_name_plural = "Materiais"
        ordering = ['-data_upload']