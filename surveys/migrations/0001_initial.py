# Generated by Django 3.2.12 on 2022-02-19 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Opis')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Ankieta',
                'verbose_name_plural': 'Ankiety',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_type', models.IntegerField(choices=[(1, 'Otwarte'), (2, 'Zamknięte (TAK/NIE)')], verbose_name='Rodzaj pytania')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Opis')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.survey', verbose_name='Ankieta')),
            ],
            options={
                'verbose_name': 'Pytanie',
                'verbose_name_plural': 'Pytania',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='Imię ankietowanego')),
                ('answers', models.TextField(verbose_name='Odpowiedzi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.survey', verbose_name='Ankieta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Odpowiedź',
                'verbose_name_plural': 'Odpowiedzi',
            },
        ),
    ]