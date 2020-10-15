import tempfile

from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.forms import modelformset_factory
from django.template.loader import render_to_string
from weasyprint import HTML, CSS

from iek import settings
from .models import ApplicationAnswer


def edit_application(request):
    AnswerFormSet = modelformset_factory(ApplicationAnswer, fields=('content',), extra=0)

    if request.method == 'POST':
        form = AnswerFormSet(request.POST)
        instances = form.save(commit=False)

        for instance in instances:
            instance.save()

    formset = AnswerFormSet(queryset=request.user.application.answers.all())

    return render(request, 'application_edit.html', {'formset': formset})


def view_application(request):
    return render(request, 'application_view.html')


def generate_pdf(request):
    html_string = render_to_string('application_pdf.html', {'user': request.user})
    html = HTML(string=html_string)
    css = CSS(filename=settings.STATIC_ROOT + '/css/print.css')
    result = html.write_pdf(stylesheets=[css])

    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=report.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response