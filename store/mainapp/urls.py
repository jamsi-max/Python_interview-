from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from .views import ProductList

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', ProductList.as_view(), name='index'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
