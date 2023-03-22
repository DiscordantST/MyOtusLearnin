from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Post


class PostModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def tearDown(self):
        self.post.delete()

    def test_title_max_length(self):
        post = Post.objects.get(id=f'{self.post.pk}')
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'user')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_get_absolute_url(self):
        post = Post.objects.get(id=f'{self.post.pk}')
        self.assertEqual(post.get_absolute_url(), f'/post/{self.post.pk}/')
