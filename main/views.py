from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

from main.models import Action, AboutImage, Specialist, Service, Contact, Application, Email, SpecialOffer, Work


def index_view(request):
    actions = Action.objects.all().order_by('number')
    slider_images = AboutImage.objects.all().order_by('number')
    specialists = Specialist.objects.all().order_by('number')
    services = Service.objects.all()
    contact = Contact.objects.last()
    works = Work.objects.all().order_by('number')
    special_offer = SpecialOffer.objects.last()

    work_list = []
    index = 0
    for item in works:
        work_list.append(tuple((index, item)))
        index = index + 1

    context = {"actions": actions, "slider_images": slider_images, "specialists": specialists, "services": services,
               "contact": contact, "special_offer": special_offer, "works": work_list}
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


@csrf_exempt
def email_application_view(request):
    email = request.POST['email']
    Email.objects.create(email=email)

    return JsonResponse(dict(success=True))
