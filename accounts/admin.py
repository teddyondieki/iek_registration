from django.contrib import admin

# Register your models here.
from accounts.models import AccountCategory, CustomAccount

admin.site.register(CustomAccount)
admin.site.register(AccountCategory)