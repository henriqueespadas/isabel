# Generated by Django 3.2.8 on 2021-10-20 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Talk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="titulo")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="descricao"),
                ),
            ],
            options={
                "verbose_name": "palestra",
                "verbose_name_plural": "palestras",
                "ordering": ("title",),
            },
        ),
    ]
