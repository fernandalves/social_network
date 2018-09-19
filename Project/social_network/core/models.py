from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ('tipo',)

    tipo = models.CharField(max_length=15)

    def __str__(self):
        return self.tipo

class Publicacao(models.Model):
    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"
        ordering = ('-dt_criacao', )

    CATEGORIAS_CHOICES = (
    )

    usuario = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=155, verbose_name="Mensagem", help_text="Digite uma mensagem")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, choices=CATEGORIAS_CHOICES)

    dt_criacao = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    dt_atualizacao = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return "%s: %s" % (self.usuario, self.mensagem)
