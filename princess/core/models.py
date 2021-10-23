from django.db import models


class Talk(models.Model):
    title = models.CharField("titulo", max_length=100)
    description = models.TextField("descricao", null=True, blank=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "palestra"
        verbose_name_plural = "palestras"

    def __str__(self):
        return self.title


class Games(models.Model):
    name = models.CharField("nome", max_length=20)
    slug = models.SlugField(max_length=30)

    class Meta:
        ordering = ("name",)
        verbose_name = "game"
        verbose_name_plural = "games"

    def __str__(self):
        return self.name


class Customers(models.Model):
    name = models.CharField("nome", max_length=80)
    ddd = models.CharField("DDD", max_length=2)
    telephone = models.CharField("telefone", max_length=11)
    address = models.TextField("endereco")
    email = models.EmailField

    class Meta:
        ordering = ("name",)
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def __str__(self):
        return self.name
