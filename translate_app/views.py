from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.utils.translation import gettext, get_language, activate


class HomeView(TemplateView):
    template_name = 'translate_app/home.html'

    def translate(self, language):
        cur_language = get_language()
        try:
            activate(language)
            text = gettext('translate_app/home.html')
        finally:
            activate(cur_language)

class NewPageView(TemplateView):
    template_name = 'translate_app/newPage.html'

    def translate(self, language):
        cur_language = get_language()
        try:
            activate(language)
            text = gettext('translate_app/newPage.html')
        finally:
            activate(cur_language)
            