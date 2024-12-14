from django.http import HttpResponse 
from django.shortcuts import render
from blogs.models import Category,Blogs
def home(request):
    
    categories= Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured= True,status='published')
    
    # print(featured_post)
    posts = Blogs.objects.filter(is_featured = False, status='published')
    # print(post)
    context={
        'categories': categories,
        'featured_post': featured_post,
        # 'post': posts
        'posts': posts

    }
    
    return render(request,'home.html',context)
    





