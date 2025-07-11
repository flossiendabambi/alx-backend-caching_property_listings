from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()
    return JsonResponse({"data": properties}, safe=False)
