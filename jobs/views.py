from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from .models import Technology, Job
import json

# Create your views here.
def technologies(request):
    if request.method == 'GET' and request.GET.get('id'):
        technologies = Technology.objects.all()
        if(technologies.count() == 0 ):
            return HttpResponseNotFound('No se encontraron tecnologías')
        else:
            selected = Technology.objects.get(id=request.GET.get('id'))
            return JsonResponse(model_to_dict(selected))
    elif request.method == 'GET':
        technologies = Technology.objects.all()
        technologies_json = serializers.serialize('json', technologies)
        return HttpResponse(technologies_json)
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        q = Technology(name=body['name'])
        q.save()
        return JsonResponse(model_to_dict(q))
    
def jobs(request):
    if request.method == 'GET' and request.GET.get('id'):
        jobs = Job.objects.all()
        filtrado = Job.objects.filter(id=request.GET.get('id'))
        if(jobs.count() == 0 and filtrado.count() == 0):
            return HttpResponseNotFound('No se encontraron trabajos')
        else:
            selected = model_to_dict(Job.objects.get(id=request.GET.get('id')))
            return JsonResponse(selected)
    elif request.method == 'GET':
        jobs = Job.objects.all()
        jobs_josn= serializers.serialize('json',jobs)
        return HttpResponse(jobs_josn)
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        technologies = Technology.objects.filter(id=body['technologies']).get()
        q = Job(
            title=body['title'],
            technologies=technologies, 
            status=body['status'], 
            published = body['published'],
            description = body['description']
            )
        q.save()
        return JsonResponse({
            "title": q.title,
            "technologies": q.technologies.name,
            "status":q.status,
            "published":q.published,
            "description":q.description
        })