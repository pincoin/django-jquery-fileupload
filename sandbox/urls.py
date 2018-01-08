from django.contrib import admin
from django.urls import path

from fileupload.views import (
    HomeView, FileUploadView
)

urlpatterns = [
    path('',
         HomeView.as_view(), name='home'),

    path('upload',
         FileUploadView.as_view(), name='upload'),

    path('admin/',
         admin.site.urls),
]
