from django import forms
from .models import Question


class imageForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['image']  # QuestionForm에서 사용할 Question 모델의 속성
