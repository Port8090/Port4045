from django import forms

class RegisterForm(forms.Form):
    image = forms.ImageField(
        error_messages={
            'required':'사진을 첨부해주세요'
        },
        label='image')