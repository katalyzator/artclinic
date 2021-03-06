# Generated by Django 2.0.7 on 2018-07-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service_type', models.CharField(choices=[('face', 'Лицо'), ('hand', 'Рука'), ('chest', 'Грудь'), ('hip', 'Бедро'), ('pussy', 'Pussy'), ('legs', 'Ноги')], max_length=20, verbose_name='Тип услуги')),
            ],
            options={
                'verbose_name': 'услугу',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
