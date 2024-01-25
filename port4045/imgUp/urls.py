from imgUp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 
app_name = "imgUp"
 
urlpatterns = [
    path("", views.펑션_파일업로드, name = "이름_파일업로드"),
]
 
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )