from django import forms
from .models import Todo


# Todo Form
class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=40,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Enter todo e.g. Delete junk files',
            'aria-label': 'Todo',
            'aria-describedby': 'add-btn'

        })
    )

# Todo form based on the Todo model
class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Enter todo e.g. Delete junk files',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn'
            })
        }
