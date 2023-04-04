from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Post, Comments
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

#For Heropage
def heroPage(request):
    return render(request, "ba/heropage.html")


#FOR THE HOMEPAGE 
def Posts(request):

    if "q" in request.GET:
        q = request.GET["q"]
        search = Q(Q(title__icontains=q) | Q(category__name__icontains=q))
        posts = Post.objects.filter(search)
    else:        
        posts = Post.objects.all()    
        
    context = {
    "posts": posts
    }
    
    return render(request, "ba/posts.html", context)
    

#FOR DETAILED POST
def postDetail(request, slug):
   
    post = Post.objects.get(slug=slug)
 
    post_comments = post.comments_set.all().order_by("-date_commented")
    
    if request.method == "POST":
        comments = Comments.objects.create(
        post=post,
        name=request.POST.get("name"),
        email=request.POST.get("email"),
        body=request.POST.get("body")        
        )
        return redirect("post-detail", slug=post.slug)


    context = {
    "post": post, "post_comments": post_comments
    }
    return render(request, "ba/post-detail.html", context)
    
    
                   
#TO DELETE COMMENTS
def deleteComment(request, pk):
    
    #post = Post.objects.get(slug=slug)
    comment = Comments.objects.get(id=pk)
    
    if request.method == "POST":
        comment.delete()
        return redirect("home")
    
    context = {
        "comment": comment,       
    }
    return render(request, "ba/delete.html", context)    


#For Contact page
def contactMe(request):

    if request.method == "POST":
        name = request.POST["name"],
        email = request.POST["email"]
        body = request.POST["body"]
        
           
        data = {
            "name": name,
            "email": email,
            "body": body
        }   
        
        message = """
        From: {}
        
        Message: {}
        """.format(data['email'], data['body'])
        
        send_mail("My Blog - Contact me",
        message,
        settings.EMAIL_HOST_USER,
        ["judeolowo1@gmail.com"],
        fail_silently=False
        )    
        return render(request, "ba/thank-you-page.html")
    
    return render(request, "ba/contact.html")

# for Email thank you page
def thankYouPage(request):
    return render(request, "ba/thank-you-page.html")  

def notFound(request, exception):
    return render(request, "ba/not-found.html")
