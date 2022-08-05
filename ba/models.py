from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.conf.urls.static import static

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 100)
    
    def __str__(self):
        return self.name
        

class Post(models.Model):
    title = models.CharField(max_length=100)

    image = models.ImageField(blank=True, null= True,upload_to="media/images/")   
    
    summary = models.CharField(max_length=100)
     
    body = models.TextField(max_length=100000)
    
    slug = models.SlugField()
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ["-date_posted"]
    
    def __str__(self):
        return self.title
        
    def summary(self):
        return self.summary

    #def snippet(self):
        #return self.body[0:10]




class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50)
    
    email = models.EmailField()
    
    body = models.TextField(null=True,blank=True)
    
    date_commented = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " = " + self.body   
    class Meta:
        ordering = ["-date_commented"]

    
#urlpatterns += static(seetings.MEDIA_URL, document_root=settings.MEDIA_ROOT  )    