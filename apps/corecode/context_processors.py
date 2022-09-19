from .models import AcademicSession, AcademicTerm, AcademicYear, SiteConfig


def site_defaults(request):
    current_session = AcademicSession.objects.get(current=True)
    current_term = AcademicTerm.objects.get(current=True)
    current_year= AcademicYear.objects.get(current=True)
    vals = SiteConfig.objects.all()
    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
        "current_year": current_year.name,

    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts
