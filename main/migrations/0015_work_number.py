# Generated by Django 2.0.7 on 2018-09-03 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_specialist_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='number',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='Порядковый номер'),
            preserve_default=False,
        ),
    ]