# Generated by Django 2.0.7 on 2018-08-08 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_specialoffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('before_image', models.ImageField(upload_to='images/works', verbose_name='Картинка (До)')),
                ('after_image', models.ImageField(upload_to='images/works', verbose_name='Картинка (После)')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Работы',
            },
        ),
    ]
