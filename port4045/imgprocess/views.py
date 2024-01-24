from django.shortcuts import render
from PIL import Image , ImageFilter
# Create your views here.
from .models import MyModel

def upload_file(request):
    if request.method == 'POST':
        my_file = request.FILES['file']
        MyModel.objects.create(my_file=my_file)
        return render(request, 'success.html')
    return render(request, 'upload_form.html')

def process_image(image_path):
    # 이미지 열기
    image = Image.open(image_path)

    # 이미지 크기 조정
    resized_image = image.resize((800, 600))

    # 필터 적용
    filtered_image = resized_image.filter(ImageFilter.GaussianBlur(radius=10))

    # 다른 포맷으로 저장
    filtered_image.save('processed_image.jpg')

    # 이미지 정보 출력
    print(f"Original Image Size: {image.size}")
    print(f"Resized Image Size: {resized_image.size}")
    print(f"Processed Image Size: {filtered_image.size}")