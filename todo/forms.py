from django import forms
from .models import Todo


class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'complete']

# class TodoDeleteForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['title']