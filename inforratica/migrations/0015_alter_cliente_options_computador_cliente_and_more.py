# Generated by Django 4.2.4 on 2023-08-01 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inforratica', '0014_cliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AddField(
            model_name='computador',
            name='cliente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='computadores', to='inforratica.cliente'),
        ),
        migrations.AlterField(
            model_name='computador',
            name='imagem',
            field=models.URLField(default='https://d2gg9evh47fn9z.cloudfront.net/1600px_COLOURBOX13277208.jpg'),
        ),
    ]
