from django.shortcuts import render, render_to_response

from main.models import Action, AboutImage, Specialist, Service, Contact


def index_view(request):
    actions = Action.objects.all()
    slider_images = AboutImage.objects.all()
    specialists = Specialist.objects.all()
    services = Service.objects.all()
    contact = Contact.objects.last()
    context = {"actions": actions, "slider_images": slider_images, "specialists": specialists, "services": services,
               "contact": contact}
    template = 'index.html'

    return render(request, template, context)


def ajax_specialist_detail_view(request, id):
    specialist = Specialist.objects.get(id=id)
    context = {
        "specialist": specialist
    }

    return render_to_response('partials/_specialist_partial.html', context)


def ajax_service_detail_view(request, id):
    service = Service.objects.get(id=id)
    context = {
        "service": service
    }

    return render_to_response('partials/_service_partial.html', context)
