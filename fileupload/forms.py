from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse

from .models import Post


class AttachmentForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


class PostForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'multiple': True,
        'class': 'my-2',
    }), required=False)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = reverse('post-create')
        self.helper.form_group_wrapper_class = 'row'
        self.helper.label_class = 'col-2 col-form-label'
        self.helper.field_class = 'col-10'
        self.helper.add_input(Submit('submit', 'Write', css_class='btn-primary'))

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body']
