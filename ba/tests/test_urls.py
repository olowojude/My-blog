from django.test import TestCase
from django.urls import reverse, resolve
from ba.views import home, detailpost, deleteComment, thankYouPage



class TestUrls(TestCase):

    def test_home_page_url(self):
        url = reverse("home")
        # below tests that the url "home" is for the home view function
        self.assertEqual(resolve(url).func, home)

    def test_detail_post_page_url(self):
        url = reverse("detailpost", args=["slug"])
        self.assertEqual(resolve(url).func, detailpost)

    def test_delete_comment_page_url(self):
        url = reverse("deleteComment", args=["pk"])
        self.assertEqual(resolve(url).func, deleteComment)
