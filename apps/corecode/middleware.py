from .models import AcademicSession, AcademicTerm, AcademicYear


class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_session = AcademicSession.objects.get(current=True)
        current_term = AcademicTerm.objects.get(current=True)
        current_year = AcademicYear.objects.get(current=True)


        request.current_session = current_session
        request.current_term = current_term
        request.current_year = current_year


        response = self.get_response(request)

        return response
