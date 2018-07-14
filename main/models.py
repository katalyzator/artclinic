from django.db import models


class Action(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'акцию'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return "{}".format(self.title)


class AboutImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название картинки')
    image = models.ImageField(upload_to='slider/images', verbose_name='Картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Картинки слайдера о нас'
        verbose_name = 'объект'

    def __str__(self):
        return "{}".format(self.title)


class Specialist(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='specialist/images', verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Специалисты'
        verbose_name = 'Специалиста'

    def __str__(self):
        return "{}".format(self.full_name)
