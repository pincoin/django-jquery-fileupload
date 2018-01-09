from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, View, ListView, DetailView
)
from django.views.generic.edit import (
    FormMixin, CreateView
)

from .forms import AttachmentForm
from .models import (
    Attachment, Post
)


class HomeView(TemplateView):
    template_name = 'fileupload/home.html'


class FileUploadView(FormMixin, View):
    form_class = AttachmentForm

    def post(self, request, *args, **kwargs):
        form = AttachmentForm(self.request.POST, self.request.FILES)

        files = []

        if form.is_valid():
            for file in request.FILES.getlist('files'):
                attachment = Attachment()

                attachment.file = file
                attachment.name = file.name
                attachment.save(**kwargs)

                files.append({
                    "pk": attachment.pk,
                    "name": file.name,
                    "size": file.size,
                    "url": attachment.file.url
                })

            data = {"files": files}

            return JsonResponse(data)
        else:
            return JsonResponse({
                'status': 'false',
                'message': 'Bad Request'
            }, status=400)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'fileupload/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'fileupload/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'body']
    template_name = 'fileupload/post_create.html'
    success_url = reverse_lazy('post-list')
