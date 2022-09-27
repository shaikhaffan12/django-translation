from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path,include
from translate_app import views
from django.conf import settings
from django.utils.translation import gettext as _

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', views.HomeView.as_view(), name='home'),
    path(_('newPage/'), views.NewPageView.as_view(), name='home'),
    )

