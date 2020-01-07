from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from .models import ReaderDefinition
from .forms import ReaderDefinitionForm

# Create your views here.


def index(request):
    return HttpResponse("its readerDefinition here !!!!!!!!!!!!")

def reader_definition_list(request):
    # readerDefinition = ReaderDefinition.objects.all()
    readerDefinition = ReaderDefinition.objects.all()
    context = {"reader": "active"}
    return render(request, 'reader_definition_list.html', {'readerDefinition': readerDefinition,'context':context})


def save_reader_definition_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            readerDefinition = ReaderDefinition.objects.all()
            data['html_reader_definition_list'] = render_to_string('includes/partial_reader_definition_list.html', {
                'readerDefinition': readerDefinition
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def reader_definition_create(request):
    if request.method == 'POST':
        form = ReaderDefinitionForm(request.POST)
    else:
        form = ReaderDefinitionForm()
    return save_reader_definition_form(request, form, 'includes/partial_reader_definition_create.html')




def reader_definition_update(request, pk):
    readerDefinition = get_object_or_404(ReaderDefinition, pk=pk)
    if request.method == 'POST':
        form = ReaderDefinitionForm(request.POST, instance=readerDefinition)
    else:
        form = ReaderDefinitionForm(instance=readerDefinition)
    return save_reader_definition_form(request, form, 'includes/partial_reader_definition_update.html')


def reader_definition_delete(request, pk):
    print (request)
    readerDefinition = get_object_or_404(ReaderDefinition, pk=pk)
    data = dict()
    if request.method == 'POST':
        readerDefinition.delete()
        data['form_is_valid'] = True
        readerDefinition = ReaderDefinition.objects.all()
        data['html_reader_definition_list'] = render_to_string('includes/partial_reader_definition_list.html', {
            'readerDefinition': readerDefinition
        })
    else:
        context = {'readerDefinition': readerDefinition}
        data['html_form'] = render_to_string('includes/partial_reader_definition_delete.html', context, request=request)
        print(data)
    return JsonResponse(data)
