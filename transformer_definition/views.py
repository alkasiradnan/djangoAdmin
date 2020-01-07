from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from .models import TransformerDefinition
from .forms import TransformerDefinitionForm
# Create your views here.


def index(request):
    return HttpResponse("its trasnformer here !!!!!!!!!!!!")

def transformer_definition_list(request):
    # transformerDefinition = TransformerDefinition.objects.all()
    transformerDefinition = TransformerDefinition.objects.all()
    context = {"transformer": "active"}
    return render(request, 'transformer_definition_list.html', {'transformerDefinition': transformerDefinition,'context':context})


def save_transformer_definition_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            transformerDefinition = TransformerDefinition.objects.all()
            data['html_transformer_definition_list'] = render_to_string('includes/partial_transformer_definition_list.html', {
                'transformerDefinition': transformerDefinition
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def transformer_definition_create(request):
    if request.method == 'POST':
        form = TransformerDefinitionForm(request.POST)
    else:
        form = TransformerDefinitionForm()
    return save_transformer_definition_form(request, form, 'includes/partial_transformer_definition_create.html')




def transformer_definition_update(request, pk):
    transformerDefinition = get_object_or_404(TransformerDefinition, pk=pk)
    if request.method == 'POST':
        form = TransformerDefinitionForm(request.POST, instance=transformerDefinition)
    else:
        form = TransformerDefinitionForm(instance=transformerDefinition)
    return save_transformer_definition_form(request, form, 'includes/partial_transformer_definition_update.html')


def transformer_definition_delete(request, pk):
    print (request)
    transformerDefinition = get_object_or_404(TransformerDefinition, pk=pk)
    data = dict()
    if request.method == 'POST':
        transformerDefinition.delete()
        data['form_is_valid'] = True
        transformerDefinition = TransformerDefinition.objects.all()
        data['html_transformer_definition_list'] = render_to_string('includes/partial_transformer_definition_list.html', {
            'transformerDefinition': transformerDefinition
        })
    else:
        context = {'transformerDefinition': transformerDefinition}
        data['html_form'] = render_to_string('includes/partial_transformer_definition_delete.html', context, request=request)
        print(data)
    return JsonResponse(data)
