from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os


class ReactAppView(View):
    def get(self, request):
        try:
            with open(str(settings.APPS_DIR.path('frontend/build/index.html'))) as file:
                return HttpResponse(file.read())
        except FileNotFoundError:
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )
