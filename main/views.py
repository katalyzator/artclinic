from django.shortcuts import render

from main.models import Action, AboutImage, Specialist


def index_view(request):
    actions = Action.objects.all()
    slider_images = AboutImage.objects.all()
    specialists = Specialist.objects.all()
    context = {"actions": actions, "slider_images": slider_images, "specialists": specialists}
    template = 'index.html'

    return render(request, template, context)
