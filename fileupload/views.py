from django.http import JsonResponse
from django.views.generic import (
    TemplateView, View
)


class HomeView(TemplateView):
    template_name = 'fileupload/home.html'


class FileUploadView(View):

    def post(self, request, *args, **kwargs):
        files = []

        for file in request.FILES.getlist('files'):
            files.append({
                "name": file.name,
                "size": file.size,
            })

        data = {"files": files}

        return JsonResponse(data)

    def form_valid(self, form):
        # self.object = form.save()
        pass
