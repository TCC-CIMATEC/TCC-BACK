# Generated by Django 3.2 on 2021-06-15 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='url_img',
            field=models.CharField(max_length=150, verbose_name='Url da questão'),
        ),
    ]
