from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image  # 사용할 모델
        fields = ['path','upload_date','detect_name']  # Image 모델에서 사용할 속성
