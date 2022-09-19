from django import forms
from django.forms import ModelForm, modelformset_factory
from django.utils.translation import gettext_lazy as _

from .models import (
    AcademicSession,
    AcademicTerm,
    AcademicYear,
    SiteConfig,
    StudentClass,
    Subject,
)

SiteConfigForm = modelformset_factory(
    SiteConfig,
    fields=(
        "key",
        "value",
    ),
    extra=0,
)


class AcademicSessionForm(ModelForm):
    prefix = _("Academic Session")

    class Meta:
        model = AcademicSession
        fields = ["name", "current"]


class AcademicTermForm(ModelForm):
    prefix = _("Academic Term")

    class Meta:
        model = AcademicTerm
        fields = ["name", "current"]
        

class AcademicYearForm(ModelForm):
    prefix = _("Academic Year")

    class Meta:
        model = AcademicYear
        fields = ["name", "current"]


class SubjectForm(ModelForm):
    prefix = _("Subject")

    class Meta:
        model = Subject
        fields = ["name"]


class StudentClassForm(ModelForm):
    prefix = _("Class")

    class Meta:
        model = StudentClass
        fields = ["name"]


class CurrentSessionForm(forms.Form):
    current_year = forms.ModelChoiceField(
        queryset=AcademicYear.objects.all(),
        help_text='Click <a href="/year/create/?next=current-session/">here</a> to add new year',
    )
    
    current_term = forms.ModelChoiceField(
        queryset=AcademicTerm.objects.all(),
        help_text='Click <a href="/term/create/?next=current-session/">here</a> to add new term',
    )


    current_session = forms.ModelChoiceField(
        queryset=AcademicSession.objects.all(),
        help_text='Click <a href="/session/create/?next=current-session/">here</a> to add new session',
    )
  