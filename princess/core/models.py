from django.db import models


class Talk(models.Model):
    title = models.CharField("titulo", max_length=100)
    description = models.TextField("descricao", null=True, blank=True)

    class Meta:
        ordering = "title"
        verbose_name = "palestra"
        verbose_name_plural = "palestras"

    def __str__(self):
        return self.title
