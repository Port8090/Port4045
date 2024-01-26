from imgUp import models
from django.shortcuts import render
from imgUp.models import imgeupload


""" def about_me(request):

  award_image = imgeupload.objects.all()

  return render(
    request, 'about.html', 
    {'award_image': award_image }
  )
 """
def about_me(request):

    award_image = imgeupload.objects.all()

    return render(
        request,
        'about.html',
        {
            'award_image': award_image
        }
    )
""" def 펑션_파일업로드(request):
    if request.method == "POST":
    #폼에서 데이터를 받아와 변수화시키기
    
        변수_업로드파일 = request.FILES["인풋_파일업로드"]
 
        # 정보를 파일에 저장하기
        변수_파일저장 = models.imgeupload(
            컬럼_파일위치 = 변수_업로드파일
        )
        변수_파일저장.save()
 
    변수_테이블의모든정보 = models.imgeupload.objects.all()
 
    return render(request, "result.html", context = {
        "키_테이블의모든정보": 변수_테이블의모든정보
    }) """


""" from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm # imageForm # RegisterForm이 정의된 경로로 수정해야 합니다.
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
"""    
""" def index(request):
    # form = imageForm()
    return render(request, 'index.html') """