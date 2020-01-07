from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from .models import WriterDefinition
from .forms import WriterDefinitionForm
# Create your views here.


def index(request):
    return HttpResponse("its trasnformer here !!!!!!!!!!!!")

def writer_definition_list(request):
    # writerDefinition = WriterDefinition.objects.all()
    writerDefinition = WriterDefinition.objects.all()
    context = {"writer": "active"}
    return render(request, 'writer_definition_list.html', {'writerDefinition': writerDefinition,'context':context})


def save_writer_definition_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            writerDefinition = WriterDefinition.objects.all()
            data['html_writer_definition_list'] = render_to_string('includes/partial_writer_definition_list.html', {
                'writerDefinition': writerDefinition
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def writer_definition_create(request):
    if request.method == 'POST':
        form = WriterDefinitionForm(request.POST)
    else:
        form = WriterDefinitionForm()
    return save_writer_definition_form(request, form, 'includes/partial_writer_definition_create.html')




def writer_definition_update(request, pk):
    writerDefinition = get_object_or_404(WriterDefinition, pk=pk)
    if request.method == 'POST':
        form = WriterDefinitionForm(request.POST, instance=writerDefinition)
    else:
        form = WriterDefinitionForm(instance=writerDefinition)
    return save_writer_definition_form(request, form, 'includes/partial_writer_definition_update.html')


def writer_definition_delete(request, pk):
    print (request)
    writerDefinition = get_object_or_404(WriterDefinition, pk=pk)
    data = dict()
    if request.method == 'POST':
        writerDefinition.delete()
        data['form_is_valid'] = True
        writerDefinition = WriterDefinition.objects.all()
        data['html_writer_definition_list'] = render_to_string('includes/partial_writer_definition_list.html', {
            'writerDefinition': writerDefinition
        })
    else:
        context = {'writerDefinition': writerDefinition}
        data['html_form'] = render_to_string('includes/partial_writer_definition_delete.html', context, request=request)
        print(data)
    return JsonResponse(data)
