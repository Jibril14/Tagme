from django import forms
from .models import Blog

from cloudinary.forms import CloudinaryFileField



class BlogForm(forms.ModelForm):
    image = CloudinaryFileField(options={
        'crop': 'thumb',
        'width': 200,
        'height': 200,
        'folder': 'tagme'
    })
    class Meta:
        model = Blog
        fields = ['title', 'description', 'tags', 'image']