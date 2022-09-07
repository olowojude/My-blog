import email
from email.mime import image
from turtle import title
from django.test import TestCase
from ba.models import Comments, Post, Category


class TestModels(TestCase):
    def setUp(self):
        # creating a category
        category = Category.objects.create(
            name="Testing"
            )

        # creating a post for testing
        post = Post.objects.create(
            title="Testing the Post model",
            image="https://bit.ly/3x4Wevw",
            body="i am testing the Post model",
            slug="testing-the-post-model",
            category = category
            )

        # creating a comment
        Comments.objects.create(
            post= post,
            name = "user",
            email = "user@gmail.com",
            body = "i love writing tests"

        )
    def test_post_name(self):
        post = Post.objects.get(title="Testing the Post model")
        self.assertTrue(post.title, "Testing the Post model")

    def test_post_category(self):
        post = Post.objects.get(title="Testing the Post model")
        self.assertEqual(post.category.name, "Testing")

    def test_post_image(self):
        post = Post.objects.get(title="Testing the Post model")
        self.assertEqual(post.image, "https://bit.ly/3x4Wevw")

    def test_post_body(self):
        post = Post.objects.get(title="Testing the Post model")
        self.assertEqual(post.body, "i am testing the Post model")



    # testing the comments
    def test_commentter_name(self):
        comment = Comments.objects.get(name="user")
        self.assertEqual(comment.name, "user")

    def test_comments_body(self):
        comment = Comments.objects.get(name="user")
        self.assertEqual(comment.body, "i love writing tests")


    def test_comment_post(self):
        comment = Comments.objects.get(name="user")
        self.assertEqual(comment.post.title,  "Testing the Post model")

    def test_comment_email(self):
        comment = Comments.objects.get(name="user")
        self.assertEqual(comment.email,  "user@gmail.com")
    

    