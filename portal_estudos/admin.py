from django.contrib import admin
from .models import Disciplina, Material

# Register your models here.
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    
    search_fields = ('nome',)
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina', 'usuario', 'data_upload')
    
    list_filter = ('disciplina', 'usuario', 'data_upload')
    
    search_fields = ('titulo', 'descricao')
    
    autocomplete_fields = ['usuario', 'disciplina']
    