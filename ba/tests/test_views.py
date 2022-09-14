from ast import arg
from email.mime import image
from http import client
from multiprocessing.connection import Client
from turtle import title
from unicodedata import category
from urllib import response
from django.test import TestCase
from django.urls import reverse, resolve
from ba.models import Category, Post, Comments
from django.test import Client


class TestViews(TestCase):


    def setUp(self):
        category = Category.objects.create(
            name="Testing"
            )
        post = Post.objects.create(
            title="Unit Tests",
            image="null",
            body="Testing testing testing",
            slug="unit-tests",
            category=category
            )
        comments = Comments.objects.create(
            post= post,
            name = "user",
            email = "user@gmail.com",
            body = "i love writing tests"
            )
        self.client = Client()
        self.home_view_url = reverse("home")
        self.detail_post_url = reverse("detailpost", args=["unit-tests"])

    def test_home_view(self):
        response = self.client.get(self.home_view_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("ba/home.html")
      
    def test_detailpost_view(self):
        response = self.client.get(self.detail_post_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("ba/detailpost.html")


    