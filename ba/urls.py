from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path("", views.heroPage, name = "home"),

    path("posts/", views.Posts, name = "posts"),
    
    path("posts/<slug:slug>/", views.postDetail, name = "post-detail"),
    
    path("delete/<str:pk>/", views.deleteComment, name="deleteComment"),

    path("contact/", views.contactMe, name = "contact-me"),

    path("contact/sent/", views.thankYouPage, name = "thank-you-page"),

    path("error/", views.notFound, name="notfound"),

]

urlpatterns += staticfiles_urlpatterns()
