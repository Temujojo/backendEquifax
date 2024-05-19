from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import json
# Create your views here.
def get_jobs(request):
    if request.method == 'GET':
        query_params = request.GET
        return JsonResponse({
            "status": '200',
            "data": {
                "name":query_params.get('name'),
                "age":query_params.get('age')
                }
            })
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        return JsonResponse({"data":body})
    else:
        return HttpResponseBadRequest('Bad request')