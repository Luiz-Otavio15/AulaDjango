from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=100)
    data = models.IntegerField()
    imagem = models.ImageField(upload_to='filmes/')
    

    def __str__(self):
        return self.titulo