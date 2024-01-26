from django.shortcuts import redirect, render
from .forms import ImageForm
from django.http import HttpResponse
from .models import ResultImage
from ultralytics import YOLO
from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile
from django.utils.text import slugify

# YOLO 모델 초기화
model = YOLO('./best_n_e15_b2_i416.pt')

def index(request):
    form = ImageForm()
    return render(request, 'index.html', {'form': form})

def create(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.save()
            # YOLO 모델을 사용하여 객체 예측
            r = model.predict(source=image_instance.image.path)[0]  # 이미지 파일의 경로에 접근
            if len(r.boxes.cls) > 0:
                cls = r.names[int(r.boxes.cls[0])]  # 객체 클래스 추출
                result_image = Image.fromarray(r.plot()).convert('RGB')
                # 이미지 파일 이름 생성
                image_name = slugify(image_instance.image.name.split('/')[-1].split('.')[0])  # 파일 경로에서 파일 이름 추출 후 slugify
                result_image_path = f"result_images/{image_name}.jpg"  # 확장자를 포함하여 파일 경로 생성
                # 결과 이미지 저장
                result_image_io = BytesIO()
                result_image.save(result_image_io, format='JPEG')
                result_image_io.seek(0)
                # 결과 이미지를 ResultImage 모델에 저장
                result_image_instance = ResultImage.objects.create(image=ImageFile(result_image_io, name=result_image_path))
                context = {'classname': cls}
                return render(request, 'result.html', context)
            else:
                # 객체가 감지되지 않은 경우에 대한 처리
                return HttpResponse("No object detected.")
    else:
        form = ImageForm()
    return redirect('foodpic')



