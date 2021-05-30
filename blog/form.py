
from .models import Post
from django.forms import HiddenInput, ModelForm

# class PostCreateForm(ModelForm):
#     class Meta:
#         model= Post
#         fields = ["title", "content", "date_posted", "author"]

#     def __init__(self, *args, **kwargs):
#         super(PostCreateForm, self).__init__(*args, **kwargs)
#         self.fields["author"].widget = HiddenInput()
#         self.fields["date_posted"].widget = HiddenInput()