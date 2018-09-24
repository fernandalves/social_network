from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    email = models.CharField(u'Mensagem', max_length=255)
    aniversario = models.DateField(u'Aniversário')
    estado = models.CharField(u'Estado', max_length=255)
    cidade = models.CharField(u'Cidade', max_length=255)
    relacionamento = models.CharField(u'Mensagem', max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

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


class Grupo(models.Model):
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ('tema', )

    criador = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    tema = models.CharField(u'Titulo do Grupo',max_length=25, blank=False)
    dt_criacao = models.DateTimeField(u'Data de criação do grupo', auto_now_add=True)
    #adicionar outros users

    def __str__(self):
        return self.tema


class Comentario(models.Model):
    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    menssagem = models.CharField(u'Mensagem', max_length=255)
    tipo = models.CharField(u'Tipo', max_length=255)
    publicacao = models.ForeignKey(Publicacao, blank=True, on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)