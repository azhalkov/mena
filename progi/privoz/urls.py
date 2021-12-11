from django.conf.urls.static import static
from django.urls import path

import seting
from seting import settings
from .views import privez


urlpatterns = [
    path('', privez, name='privoz'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)