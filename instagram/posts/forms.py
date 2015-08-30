from __future__ import absolute_import

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('photo', 'caption', )
        model = Post

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'photo',
            'caption',
            Submit('submit', 'Submit', css_class='btn primary')
        )
