from django.http import JsonResponse
from django.views.generic import (
    TemplateView, View, ListView, DetailView
)
from django.views.generic.edit import (
    FormMixin, CreateView
)

from .forms import (
    AttachmentForm, PostForm, PostAttachmentForm
)
from .models import (
    Attachment, Post
)


class HomeView(TemplateView):
    template_name = 'fileupload/home.html'


class FileUploadView(FormMixin, View):
    form_class = AttachmentForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

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
    template_name = 'fileupload/post_create.html'

    def get_form_class(self):
        if self.request.method == 'POST':
            # Hidden fields for attachments must be validated.
            return PostAttachmentForm
        else:
            # Hidden fields are not prepopulated but appended to form by AJAX.
            return PostForm

    def form_valid(self, form):
        response = super().form_valid(form)

        # TODO: limit number

        # Attachments are not related to any post yet.
        attachments = Attachment.objects.filter(
            pk__in=form.cleaned_data['attachments'],
            post__isnull=True,
        )
        self.object.attachments.set(attachments)

        return response

class PostCreateView2(PostCreateView):
    template_name = 'fileupload/post_create2.html'