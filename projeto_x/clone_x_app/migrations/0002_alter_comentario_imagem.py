# Generated by Django 5.0.6 on 2024-06-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone_x_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='imagem',
            field=models.ImageField(default='imagens_comentarios/0aa90a1e1dd37911a74556afaed4c2bf.jpg', upload_to='imagens_comentarios/'),
        ),
    ]
