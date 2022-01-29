from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('events/', include('events.urls')),
    ]))
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
