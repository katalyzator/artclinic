from django.shortcuts import render

from main.models import Action, AboutImage, Specialist, Service


def index_view(request):
    actions = Action.objects.all()
    slider_images = AboutImage.objects.all()
    specialists = Specialist.objects.all()
    services = Service.objects.all()
    context = {"actions": actions, "slider_images": slider_images, "specialists": specialists, "services": services}
    template = 'index.html'

    return render(request, template, context)
