from django.http import HttpResponse
from .updatepo import update_po


def translate(request):
    update_po(request.POST)
    return HttpResponse()
