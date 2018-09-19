from django.contrib import admin
from .models import Publicacao, Categoria, Grupo

@admin.register(Comentario)
@admin.register(Usuario)

@admin.register(Categoria)
class Categoria_Admin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('tipo',)
        }),
    )

@admin.register(Publicacao)
class Publicacao_Admin(admin.ModelAdmin):
    list_display = ('usuario', 'mensagem', 'dt_criacao', 'categoria',)
    search_fields = ('mensagem', 'usuario__email', 'categoria' )
    list_filter = ('usuario', 'categoria', )

    fieldsets = (
        (None, {
            'fields': ('mensagem', )
        }),
        ('Categoria', {
            'fields': ('categoria',)
        }),
        ("Dados", {
            'fields': (('dt_criacao', 'dt_atualizacao', ), )
        }),
    )
    readonly_fields = ('dt_criacao', 'dt_atualizacao', 'slug',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

@admin.register(Grupo)
class Grupo_Admin(admin.ModelAdmin):
    list_filter = ('criador', 'tema',)
    fieldsets = (
        (None, {
            'fields': ('tema',)
        }),
        ("outros", {
            'fields': (('dt_criacao', ), )
        }),
    )
    readonly_fields = ('dt_criacao',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.criador = request.user
        super().save_model(request, obj, form, change)