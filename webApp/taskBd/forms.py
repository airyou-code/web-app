import imp
from .models import taskiq
from django.forms import ModelForm

class taskiqForm(ModelForm):
    class Meta:
        model = taskiq
        fields = ['question', 'corAnsver', 'answer1',
                  'answer2', 'answer3', 'answer4', 'answer5', 'answer6']
