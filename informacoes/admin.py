from django.contrib import admin
from .models import Compromisso, Agenda
# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

admin.site.register(Agenda, AgendaAdmin)

class CompromissoAdmin(admin.ModelAdmin):
    list_display = ('data', 'endereco', 'telefone')

admin.site.register(Compromisso, CompromissoAdmin)