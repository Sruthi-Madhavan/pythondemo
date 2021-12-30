from django import forms

from todoapps.models import Tasktodo


class TodoForm(forms.ModelForm):
    class Meta:
        model=Tasktodo
        fields=['name','priority','date']