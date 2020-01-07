from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from configurations.models import Configuration
from .service import activemq

# Create your views here.

def configuration_list(request):
    # configuration = Configuration.objects.all()
    configuration = Configuration.objects.all()
    context = {"configuration": "active"}
    return render(request, 'operation_list.html', {'operation': configuration,'context':context})



def index(request, pk):
    print("its operation here")
    operation = get_object_or_404(Operation, pk=1)
    data = dict()
    data['readerType']=operation.configurations.reader.type
    data['readerPath'] = operation.configurations.reader.path
    data['transformerPath']= operation.configurations.transformer.path

    activemq.send(body=data, destination='/queue/feederAMQ')
    return HttpResponse('Success!')
