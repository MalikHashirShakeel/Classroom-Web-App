from django import forms
from .models import Classroom

# Form to create a new classroom
class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'class_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-purple'}),
            'class_code': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-purple'}),
        }


# Form to join a classroom
class JoinClassroomForm(forms.Form):
    class_code = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-purple',
            'placeholder': 'Enter Class Code'
        }),
        label='Class Code'
    )