from django.contrib import admin

from main.models import Action, AboutImage, Specialist, Email, Service, Specialization, Course, Contact

admin.site.site_header = 'Панель управления сайтом ArtClinic'

admin.site.register(Action)
admin.site.register(AboutImage)
admin.site.register(Specialist)
admin.site.register(Email)
admin.site.register(Service)
admin.site.register(Specialization)
admin.site.register(Course)
admin.site.register(Contact)
