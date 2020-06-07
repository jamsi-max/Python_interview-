from django.urls import path, re_path

import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
