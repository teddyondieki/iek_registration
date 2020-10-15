from django.conf.urls import url

from .views import edit_application, view_application, generate_pdf

urlpatterns = [
    url(r'^application/edit', edit_application, name='edit_application'),
    url(r'^application/view', view_application, name='view_application'),
    url(r'^application/pdf$', generate_pdf, name='generate_pdf'),

]