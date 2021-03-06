from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms.models import inlineformset_factory

from .models import (
    Post, Attachment
)


class AttachmentForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}), required=False)


class AttachmentInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AttachmentInlineForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_group_wrapper_class = 'row'
        self.helper.label_class = 'col-2 col-form-label'
        self.helper.field_class = 'col-10'

    class Meta:
        model = Attachment
        fields = ['name', 'file']


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False  # disable form tag
        self.helper.form_group_wrapper_class = 'row'
        self.helper.label_class = 'col-2 col-form-label'
        self.helper.field_class = 'col-10'

    class Meta:
        model = Post
        fields = ['title', 'body']


class PostFileForm(PostForm):
    files = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True, 'class': 'my-2'}), required=False)


class PostFileAttachmentForm(PostFileForm):
    attachments = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def clean_attachments(self):
        data = self.data.getlist('attachments')

        if not data and not all(isinstance(item, int) for item in data):
            raise forms.ValidationError("PK must be integers.")

        return data


AttachmentInlineFormSet = inlineformset_factory(
    Post, Attachment,
    form=AttachmentInlineForm,
    fields=['file', 'name'],
    extra=2,
)
