from django.shortcuts import redirect, render
from .forms import ImageForm
from django.http import HttpResponse
from .models import ResultImage
from ultralytics import YOLO
from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile
from django.utils.text import slugify
from django.conf import settings  # settings 모듈 임포트
import numpy as np

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
            form.save()
            # 이미지를 BGR 형식으로 변환
            image_bgr = Image.open(form.instance.image.path).convert('RGB')  # 이미지 로드 및 RGB로 변환
            image_bgr = np.array(image_bgr)[:, :, ::1].copy()  # RGB를 BGR로 변환
            # YOLO 모델을 사용하여 객체 예측
            r = model.predict(source=image_bgr)[0]
            # YOLO 모델을 사용하여 객체 예측
            if len(r.boxes.cls) > 0:
                cls = r.names[int(r.boxes.cls[0])]  # 객체 클래스 추출
                result_image = Image.fromarray(r.plot()).convert('RGB')
                result_image_path = "static/result.jpg"
                result_image.save(result_image_path)
                context = {'classname': cls}
                return render(request, 'result.html', context)
            else:
                # 객체가 감지되지 않은 경우에 대한 처리
                return HttpResponse("No object detected.")
    else:
        form = ImageForm()
    return redirect('foodpic')
