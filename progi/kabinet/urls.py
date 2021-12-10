# progi/kabinet/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import form_status, post_new

urlpatterns = [
    path('', TemplateView.as_view(template_name='kabinet/kabinet.html'), name='kabinet'),
    path('categori_form/', form_status, name='categori_form'),
    path('categori_form1/', post_new, name='categori_form1'),
]

