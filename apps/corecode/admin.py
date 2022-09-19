from django.contrib import admin
from apps.corecode.models import AcademicTerm, AcademicYear, SiteConfig, Subject
# Register your models here.

admin.site.register(AcademicYear)
admin.site.register(AcademicTerm)

admin.site.register(Subject)
admin.site.register(SiteConfig)

