# Generated by Django 3.2.8 on 2021-10-23 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customers",
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
                ("name", models.CharField(max_length=80, verbose_name="nome")),
                ("ddd", models.CharField(max_length=2, verbose_name="DDD")),
                ("telephone", models.CharField(max_length=11, verbose_name="telefone")),
                ("address", models.TextField(verbose_name="endereco")),
            ],
            options={
                "verbose_name": "customer",
                "verbose_name_plural": "customers",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Games",
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
                ("name", models.CharField(max_length=20, verbose_name="nome")),
                ("slug", models.SlugField(max_length=30)),
            ],
            options={
                "verbose_name": "game",
                "verbose_name_plural": "games",
                "ordering": ("name",),
            },
        ),
    ]