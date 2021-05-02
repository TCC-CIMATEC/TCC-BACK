# Generated by Django 3.2 on 2021-05-02 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jogador', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogador',
            options={'verbose_name': 'Jogador', 'verbose_name_plural': 'Jogadores'},
        ),
        migrations.RemoveField(
            model_name='jogador',
            name='faseatualraciociniologico',
        ),
        migrations.AddField(
            model_name='jogador',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='authenticate.user', verbose_name='Usuário'),
            preserve_default=False,
        ),
    ]
