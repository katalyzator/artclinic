from ckeditor.fields import RichTextField
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


class Specialization(models.Model):
    title = models.CharField(max_length=255, verbose_name='Специализации')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Список специализаций'
        verbose_name = 'объект'

    def __str__(self):
        return "{}".format(self.title)


class Course(models.Model):
    title = models.CharField(max_length=400, verbose_name='Наименование')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'Образование и курсы специалистов'

    def __str__(self):
        return "{}".format(self.title)


class Specialist(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='specialist/images', verbose_name='Картинка')
    experience = models.PositiveIntegerField(default=1, verbose_name='Стаж работы (лет)')
    specialization = models.ManyToManyField(Specialization, null=True, related_name='specialization',
                                            verbose_name='Список специализаций')
    courses = models.ManyToManyField(Course, null=True, related_name='courses', verbose_name='Образование и курсы')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Специалисты'
        verbose_name = 'Специалиста'

    def __str__(self):
        return "{}".format(self.full_name)


class Email(models.Model):
    email = models.EmailField(verbose_name='Email')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Emails'
        verbose_name = 'email'

    def __str__(self):
        return "{}".format(str(self.email))


class Service(models.Model):
    SERVICE_CHOICES = (
        ("face", "Лицо"),
        ("hand", "Рука"),
        ("chest", "Грудь"),
        ("hip", "Бедро"),
        ("pussy", "Pussy"),
        ("legs", "Ноги")
    )

    SERVICE_CATEGORY = (
        ("cosmetology", "Косметология"),
        ("surgery", "Хирургия")
    )
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, verbose_name='Тип услуги')
    service_category = models.CharField(max_length=20, choices=SERVICE_CATEGORY, verbose_name='Категория услуги')

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'услугу'

    def __str__(self):
        return "{}".format(self.title)


class Contact(models.Model):
    text = RichTextField(verbose_name='Контент')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'объект'

    def __str__(self):
        return "Контакты {}".format(str(self.id))
