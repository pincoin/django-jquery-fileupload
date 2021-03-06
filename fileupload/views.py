from django.db import transaction
from django.http import JsonResponse
from django.views.generic import (
    TemplateView, View, ListView, DetailView
)
from django.views.generic.edit import (
    FormMixin, CreateView, UpdateView
)

from .forms import (
    AttachmentForm, PostFileForm, PostFileAttachmentForm, PostForm, AttachmentInlineFormSet
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
            return PostFileAttachmentForm
        else:
            # Hidden fields are not prepopulated but appended to form by AJAX.
            return PostFileForm

    def form_valid(self, form):
        response = super().form_valid(form)

        # Attachments are not related to any post yet.
        attachments = Attachment.objects.filter(
            pk__in=form.cleaned_data['attachments'],
            post__isnull=True,
        )
        self.object.attachments.set(attachments)

        return response


class PostCreateView2(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'fileupload/post_create2.html'

    def get_context_data(self, **kwargs):
        context = super(PostCreateView2, self).get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = AttachmentInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = AttachmentInlineFormSet

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        with transaction.atomic():
            self.object = form.save()

            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)


class PostCreateView3(PostCreateView):
    template_name = 'fileupload/post_create3.html'

    def get_form_class(self):
        if self.request.method == 'POST':
            # Hidden fields for attachments must be validated.
            return PostFileAttachmentForm
        else:
            # Hidden fields and file input are not prepopulated but appended to form by AJAX.
            return PostForm


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'fileupload/post_update.html'

    def get_form_class(self):
        if self.request.method == 'POST':
            # Hidden fields for attachments must be validated.
            return PostFileAttachmentForm
        else:
            # Hidden fields are not prepopulated but appended to form by AJAX.
            return PostFileForm

    def form_valid(self, form):
        response = super().form_valid(form)

        # Attachments are not related to any post yet.
        attachments = Attachment.objects.filter(
            pk__in=form.cleaned_data['attachments'],
            post__isnull=True,
        )
        self.object.attachments.set(attachments)

        return response


class PostUpdateView3(PostUpdateView):
    template_name = 'fileupload/post_update3.html'

    def get_form_class(self):
        if self.request.method == 'POST':
            # Hidden fields for attachments must be validated.
            return PostFileAttachmentForm
        else:
            # Hidden fields and file input are not prepopulated but appended to form by AJAX.
            return PostForm
