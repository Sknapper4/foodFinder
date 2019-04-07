from django.http import HttpResponse
from django.template import loader

from .models import Snack, Store


def index(request):
    snack_list = Snack.objects.all()[:5]
    template = loader.get_template('food/index.html')
    context = {
        'snack_list': snack_list,
    }
    return HttpResponse(template.render(context, request))
