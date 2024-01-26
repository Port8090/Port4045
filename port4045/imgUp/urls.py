from imgUp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 
app_name = "imgUp"
 
urlpatterns = [
    path("", views.about_me, name = "about_me"),
]
 
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )