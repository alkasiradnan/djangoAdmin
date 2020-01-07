from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from .models import Configuration
from .forms import ConfigurationForm
# Create your views here.


def index(request):
    return HttpResponse("its configuration here !!!!!!!!!!!!")

def configuration_list(request):
    # configuration = Configuration.objects.all()
    configuration = Configuration.objects.all()
    context = {"configuration": "active"}
    return render(request, 'configuration_list.html', {'configuration': configuration,'context':context})


def save_configuration_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            configuration = Configuration.objects.all()
            data['html_configuration_list'] = render_to_string('includes/partial_configuration_list.html', {
                'configuration': configuration
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def configuration_create(request):
    if request.method == 'POST':
        form = ConfigurationForm(request.POST)
    else:
        form = ConfigurationForm()
    return save_configuration_form(request, form, 'includes/partial_configuration_create.html')




def configuration_update(request, pk):
    print ("pkkkk",pk)
    configuration = get_object_or_404(Configuration, pk=pk)
    if request.method == 'POST':
        form = ConfigurationForm(request.POST, instance=configuration)
    else:
        form = ConfigurationForm(instance=configuration)
    return save_configuration_form(request, form, 'includes/partial_configuration_update.html')


def configuration_delete(request, pk):
    print (request)
    configuration = get_object_or_404(Configuration, pk=pk)
    data = dict()
    if request.method == 'POST':
        configuration.delete()
        data['form_is_valid'] = True
        configuration = Configuration.objects.all()
        data['html_configuration_list'] = render_to_string('includes/partial_configuration_list.html', {
            'configuration': configuration
        })
    else:
        context = {'configuration': configuration}
        data['html_form'] = render_to_string('includes/partial_configuration_delete.html', context, request=request)
        print(data)
    return JsonResponse(data)
