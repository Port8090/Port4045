from django import forms
from .models import Image


class imageForm(forms.ModelForm):
    class Meta:
        model = Image  # 사용할 모델
        fields = ['path']  # Image 모델에서 사용할 속성