from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagem = models.ImageField(upload_to ='produtos/', blank=True, null=True)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome