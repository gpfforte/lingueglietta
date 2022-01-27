from django.forms import inlineformset_factory, BaseInlineFormSet, models
from .models import Post, Comment
from django.forms.widgets import HiddenInput
from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _


class PostForm(models.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', ]
        labels = {
            'content': _('Post Content'),
        }
        help_texts = {
            'content': _('Insert Post Content'), }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': '5',
                'cols': '90',
                'maxlength': '200',
            }),
        }
        labels = {
            'content': _('Comment'),
        }
        help_texts = {
            'content': _('Insert Post Comment'), }

    # def __init__(self, *args, **kwargs):
    #     # self.author_init = kwargs.pop('user', None)
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     # self.init_author = kwargs['author']
    #     # print(self.author_init)
    #     # self.fields['author'].widget = HiddenInput()

    # def clean(self):
    #     cleaned_data = super(PostForm, self).clean()
    #     author = cleaned_data.get('author')
        # print(author)
        # print(self.author_init)
        # if self.author_init != author:
        #     raise forms.ValidationError('There is a problem with the author')
        # return cleaned_data

# class CommentForm(models.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['content','author','post']
#     def __init__(self, *args, **kwargs):
#         super(CommentForm, self).__init__(*args, **kwargs)
#         self.fields['author'].widget = HiddenInput()
#         self.fields['post'].widget = HiddenInput()
