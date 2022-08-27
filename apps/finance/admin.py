from django.contrib import admin

from apps.finance.models import Invoice, Receipt

# Register your models here.

admin.site.register(Invoice)
admin.site.register(Receipt)