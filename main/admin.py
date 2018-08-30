from django.contrib import admin

from main.models import Action, AboutImage, Specialist, Email, Service, Specialization, Course, Contact, Application, \
    SpecialOffer, Work

admin.site.site_header = 'Панель управления сайтом ArtClinic'


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'experience', 'number']
    list_editable = ['number']

    class Meta:
        model = Specialist


admin.site.register(Action)
admin.site.register(AboutImage)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Email)
admin.site.register(Service)
admin.site.register(Specialization)
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Application)
admin.site.register(SpecialOffer)
admin.site.register(Work)
