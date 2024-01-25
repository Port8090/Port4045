from django.shortcuts import render
from PIL import Image , ImageFilter
# Create your views here.
from .models import MyModel, Post, Photo
from django.utils import timezone
from Flask import redirect
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

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.user = request.user
        post.save()
        # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다 
        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
        return redirect('/detail/' + str(post.id))
    else:
        return render(request, 'new.html')