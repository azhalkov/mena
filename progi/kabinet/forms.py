#  progi/kabinet/forms

from django import forms
from progi.kabinet.models import Status


class StatusForm(forms.ModelForm):
    title = forms.CharField(max_length=100)

    class Meta:
        model = Status
        fields = ('title',)
        template_name = 'kabinet/status_form.html'


