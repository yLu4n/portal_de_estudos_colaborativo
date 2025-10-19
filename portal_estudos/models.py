from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Material(models.Model):
    """
    Representa um arquivo de estudo 
    enviado por um usuário e associado 
    a uma disciplina.
    """
    
    MATEMATICA = 'MAT'
    PORTUGUES = 'POR'
    FISICA = 'FIS'
    QUIMICA = 'QUI'
    BIOLOGIA = 'BIO'
    INGLES = 'ING'
    ARTES = 'ART'
    FILOSOFIA = 'FIL'
    GEOGRAFIA = 'GEO'
    HISTORIA = 'HIS'
    ESTUDO_ORIENTADO_DE_PORTUGUES = 'EOP'
    ESTUDO_ORIENTADO_DE_MATEMATICA = 'EOM'
    EDUCACAO_FISICA = 'EDF'
    CIVISMO = 'CIV'
    SOCIOLOGIA = 'SOC'
    
    LISTA_DE_DISCIPLINAS = [
        (MATEMATICA, 'Matemática'),
        (PORTUGUES, 'Português'),
        (FISICA, 'Física'),
        (QUIMICA, 'Química'),
        (BIOLOGIA, 'Biologia'),
        (INGLES, 'Inglês'),
        (ARTES, 'Artes'),
        (FILOSOFIA, 'Filosofia'),
        (GEOGRAFIA, 'Geografia'),
        (HISTORIA, 'História'),
        (ESTUDO_ORIENTADO_DE_PORTUGUES, 'Estudo Orientado de Português'),
        (ESTUDO_ORIENTADO_DE_MATEMATICA, 'Estudo Orientado de Matemática'),
        (EDUCACAO_FISICA, 'Educação Física'),
        (CIVISMO, 'Civismo'),
        (SOCIOLOGIA, 'Sociologia'),
    ]
    
    
    titulo = models.CharField(max_length=255, help_text="Título do material de estudo")
    descricao = models.TextField(blank=True, help_text="Descrição opcional do material", null=True)
    arquivo = models.FileField(upload_to='materiais/', help_text="Arquivo do material de estudo")
    data_upload = models.DateTimeField(auto_now=True)
    
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null= True,
        blank= True,
        related_name='materiais enviados'
    )
    
    disciplina = models.CharField(
        max_length=3,
        choices= LISTA_DE_DISCIPLINAS,
        default=MATEMATICA
    )
    
    def __str__(self):
        return f'{self.titulo} - {self.get_disciplina_display()}'
    
