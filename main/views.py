from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

from main.models import Action, AboutImage, Specialist, Service, Contact, Application


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


@csrf_exempt
def application_view(request):
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    Application.objects.create(name=name, phone_number=phone_number)

    return JsonResponse(dict(success=True))
