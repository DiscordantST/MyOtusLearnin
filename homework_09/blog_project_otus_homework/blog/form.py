from django.forms import ModelForm

from blog.models import Post


class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите заголовок'})
        self.fields['author'].widget.attrs.update(
            {'class': 'form-select'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите текст поста', 'rows': 3})


class UpdatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'body'
                  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите заголовок'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите текст поста', 'rows': 3})
