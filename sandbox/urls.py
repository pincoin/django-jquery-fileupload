from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from fileupload.views import (
    HomeView, FileUploadView, PostListView, PostDetailView, PostCreateView, PostCreateView2
)

urlpatterns = [
    path('',
         HomeView.as_view(), name='home'),

    path('upload',
         FileUploadView.as_view(), name='file-upload'),

    path('posts',
         PostListView.as_view(), name='post-list'),

    path('posts/<int:pk>',
         PostDetailView.as_view(), name='post-detail'),

    path('posts/create',
         PostCreateView.as_view(), name='post-create'),

    path('posts/create-html',
         PostCreateView2.as_view(), name='post-create-2'),

    path('admin/',
         admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
