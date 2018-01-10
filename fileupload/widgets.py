from django.forms import widgets


class AjaxFileUploadWidget(widgets.FileInput):
    template_name = 'fileupload/widgets/ajax_file_upload_widget.html'

    def get_context(self, name, value, attrs):
        context = super(AjaxFileUploadWidget, self).get_context(name, value, attrs)
        context['widget']['attrs']['multiple'] = True
        return context

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)
        print(context)
        print(context.get('csrf_token'))
        return self._render(self.template_name, context, renderer)
