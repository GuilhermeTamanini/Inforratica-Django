# Generated by Django 4.2.6 on 2023-10-06 17:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nome", models.CharField(max_length=50)),
                ("cpf", models.CharField(max_length=11)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=50)),
                ("endereco", models.CharField(max_length=50)),
                (
                    "senha",
                    models.CharField(
                        default="",
                        max_length=30,
                        validators=[django.core.validators.MinLengthValidator(4)],
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Clientes",
            },
        ),
        migrations.CreateModel(
            name="Computador",
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
                ("placa_mae", models.CharField(max_length=50)),
                ("processador", models.CharField(max_length=50)),
                ("memoria_ram", models.CharField(max_length=80)),
                ("cooler", models.CharField(default="Stock", max_length=50)),
                ("hd", models.CharField(max_length=50)),
                ("ssd", models.CharField(max_length=50)),
                ("fonte", models.CharField(max_length=50)),
                ("gabinete", models.CharField(max_length=50)),
                ("placa_de_video", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Notebook",
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
                ("marca", models.CharField(max_length=50)),
                ("modelo", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="OrdemServico",
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
                ("data", models.DateField(auto_now_add=True)),
                ("descricao", models.TextField(max_length=500)),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2, default=None, max_digits=10, null=True
                    ),
                ),
                (
                    "computador",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ordensservico",
                        to="inforratica.computador",
                    ),
                ),
                (
                    "notebook",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ordensservico",
                        to="inforratica.notebook",
                    ),
                ),
            ],
        ),
    ]
