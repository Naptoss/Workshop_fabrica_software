from django.contrib import admin
from .models import jogo, loja

class jogosAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")

admin.site.register(jogo, jogosAdmin)

class lojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "endereco", "telefone")

admin.site.register(loja,lojaAdmin)