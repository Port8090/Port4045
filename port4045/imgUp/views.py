from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm  # RegisterForm이 정의된 경로로 수정해야 합니다.
from .models import Product  # Product 모델이 정의된 경로로 수정해야 합니다.

# Create your views here.
class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = '/product/list'

    def form_valid(self, form):
        product = Product(
            product = form.cleaned_data.get('product'),
            price = form.cleaned_data.get('price'),
            description = form.cleaned_data.get('description'),
            stock = form.cleaned_data.get('stock'),
            image = form.cleaned_data.get('image')
        )
        product.save()
        return super().form_valid(form)