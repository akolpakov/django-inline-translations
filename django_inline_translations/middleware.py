from django.utils.translation import LANGUAGE_SESSION_KEY


class SaveLocaleToSessionMiddleware(object):
    def process_request(self, request):
        request.session[LANGUAGE_SESSION_KEY] = request.LANGUAGE_CODE
