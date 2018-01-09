from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from fileupload.views import (
    HomeView, FileUploadView, PostListView, PostDetailView
)

urlpatterns = [
    path('',
         HomeView.as_view(), name='home'),

    path('upload',
         FileUploadView.as_view(), name='file-upload'),

    path('posts',
         PostListView.as_view(), name='post-list'),

    path('posts/<str:slug>',
         PostDetailView.as_view(), name='post-detail'),

    path('admin/',
         admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
