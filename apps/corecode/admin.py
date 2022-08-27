from django.contrib import admin
from apps.corecode.models import AcademicTerm, AcademicYear
# Register your models here.

admin.site.register(AcademicYear)
admin.site.register(AcademicTerm)

