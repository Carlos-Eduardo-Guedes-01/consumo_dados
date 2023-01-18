from django.contrib import admin
from .models import Cliente

class MulheresMereen(admin.ModelAdmin):
    list_display = ('codigo','nome','sobrenome','sexo','altura','peso','nascimento','estado','cidade','bairro','numero')
    list_display_links = ('codigo', 'nome')
    search_fields = ('nome',)
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(Cliente, MulheresMereen)
