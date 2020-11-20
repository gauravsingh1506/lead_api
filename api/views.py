from django.shortcuts import render
from .models import Lead
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse

# Create your views here.
def fetch(request, lead_id):
    try:
        obj = Lead.objects.get(pk=lead_id)
    except:
        raise Http404("{}")
    else:
        object = {
            "id": str(lead_id),
            "first_name": obj.first_name,
            "last_name": obj.last_name,
            "mobile": obj.mobile,
            "email": obj.email,
            "location_type": obj.location_type,
            "location_string": obj.location_string,
            "status": obj.status,
            "communication": obj.communication
        }
        print(object)
        return JsonResponse(object)


