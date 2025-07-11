from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values('title', 'description', 'price', 'location', 'created_at')
    return JsonResponse(list(properties), safe=False)
