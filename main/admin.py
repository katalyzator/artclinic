from django.contrib import admin

from main.models import Action, AboutImage, Specialist, Email, Service, Specialization, Course, Contact, Application, \
    SpecialOffer, Work

admin.site.site_header = 'Панель управления сайтом ArtClinic'


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'experience', 'number']
    list_editable = ['number']

    class Meta:
        model = Specialist


class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'number', 'timestamp']
    list_editable = ['number']

    class Meta:
        model = Work


class ActionAdmin(admin.ModelAdmin):
    list_display = ['title', 'number']
    list_editable = ['number']

    class Meta:
        model = Action


class AboutImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'number']
    list_editable = ['number']

    class Meta:
        model = AboutImage


admin.site.register(Work, WorkAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(AboutImage, AboutImageAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Email)
admin.site.register(Service)
admin.site.register(Specialization)
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Application)
admin.site.register(SpecialOffer)
