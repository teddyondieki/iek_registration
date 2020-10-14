from django.contrib import admin
from .models import *

admin.site.register(Application)
admin.site.register(ApplicationAnswer)
admin.site.register(ApplicationCategory)
admin.site.register(ApplicationQuestion)