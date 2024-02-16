from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import RublesRate
from .utils import convert_rate_obj_to_json


def get_rate(request):
    charcode = request.GET.get('charcode', '')
    date = request.GET.get('date', '')
    rate = get_object_or_404(RublesRate, charcode=charcode, date=date)
    return HttpResponse(convert_rate_obj_to_json(rate), content_type="application/json")
