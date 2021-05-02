# Generated by Django 3.2 on 2021-05-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categoria',
            field=models.CharField(blank=True, choices=[('P', 'Professor'), ('A', 'Aluno')], max_length=1, null=True, verbose_name='Categoria do usuario'),
        ),
    ]