# Generated by Django 3.2 on 2021-05-19 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jogador', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('nome', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome da turma')),
                ('turno', models.CharField(blank=True, choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno'), ('I', 'Integral')], max_length=1, null=True, verbose_name='Turno da turma')),
                ('codigoTurma', models.CharField(blank=True, max_length=30, null=True, verbose_name='Código da turma')),
                ('alunos', models.ManyToManyField(blank=True, null=True, related_name='AlunosTurma', to='jogador.Jogador', verbose_name='Alunos da turma')),
                ('professor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Professor', to=settings.AUTH_USER_MODEL, verbose_name='Professor')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
    ]
