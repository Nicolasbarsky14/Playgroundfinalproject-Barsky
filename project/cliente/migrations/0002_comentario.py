# Generated by Django 5.0.1 on 2024-01-31 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cliente", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comentario",
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
                ("autor", models.CharField(max_length=100)),
                ("contenido", models.TextField()),
                (
                    "fecha_comentario",
                    models.DateTimeField(verbose_name="Fecha de comentario"),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="comentarios",
                        to="cliente.cliente",
                    ),
                ),
            ],
        ),
    ]
