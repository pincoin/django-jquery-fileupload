from django.http import JsonResponse
from django.views.generic import (
    TemplateView, View
)
from django.views.generic.edit import FormMixin


class HomeView(TemplateView):
    template_name = 'fileupload/home.html'


class FileUploadView(FormMixin, View):

    def post(self, request, *args, **kwargs):
        data = {"files": [
            {
                "name": "picture1.jpg",
                "size": 902604,
                "url": "http:\/\/example.org\/files\/picture1.jpg",
                "thumbnailUrl": "http:\/\/example.org\/files\/thumbnail\/picture1.jpg",
                "deleteUrl": "http:\/\/example.org\/files\/picture1.jpg",
                "deleteType": "DELETE",
                "pk": 1,
            },
            {
                "name": "picture2.jpg",
                "size": 841946,
                "url": "http:\/\/example.org\/files\/picture2.jpg",
                "thumbnailUrl": "http:\/\/example.org\/files\/thumbnail\/picture2.jpg",
                "deleteUrl": "http:\/\/example.org\/files\/picture2.jpg",
                "deleteType": "DELETE",
                "pk": 2,
            }
        ]}
        return JsonResponse(data)

    def form_valid(self, form):
        # self.object = form.save()
        pass
