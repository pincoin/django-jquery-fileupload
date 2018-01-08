from django.http import JsonResponse
from django.views.generic import (
    TemplateView, View
)

from .models import Attachment


class HomeView(TemplateView):
    template_name = 'fileupload/home.html'


class FileUploadView(View):

    def post(self, request, *args, **kwargs):
        files = []

        for file in request.FILES.getlist('files'):
            attachment = Attachment()

            attachment.file = file
            attachment.name = file.name
            attachment.save(**kwargs)

            files.append({
                "pk": attachment.pk,
                "name": file.name,
                "size": file.size,
            })

        data = {"files": files}

        return JsonResponse(data)

    def form_valid(self, form):
        # self.object = form.save()
        pass
