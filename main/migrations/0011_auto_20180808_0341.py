# Generated by Django 2.0.7 on 2018-08-08 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='specialization',
            field=models.ManyToManyField(related_name='specialization', to='main.Specialization', verbose_name='Список специализаций'),
        ),
    ]
