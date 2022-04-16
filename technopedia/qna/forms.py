from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['user', 'title', 'description']
        widgets = {'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the id', 'value': '1', 'type': 'hidden'}),
                   'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'})}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['user', 'queid', 'answer']
        widgets = {'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the id', 'readonly': 'readonly', 'value': '1', 'type': 'hidden'}),
                   'queid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Question Number', 'readonly': 'readonly', 'type': 'hidden'}),
                   'answer': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type Your Answer Here....'})}

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['queid'].required = False


class StatusQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['status']
        widgets = {'status': forms.Select(attrs={'class': 'form-control'})}
