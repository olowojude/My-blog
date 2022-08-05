from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [

    path("", views.home, name = "home"),
    
    path("<slug:slug>/", views.detailpost, name = "detailpost"),
    
    path("delete-comment/<str:pk>/", views.deleteComment, name="deleteComment")
]

urlpatterns += staticfiles_urlpatterns()

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)