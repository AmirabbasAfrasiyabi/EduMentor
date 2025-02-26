from django.shortcuts import render
from django.http import HttpResponse , JsonResponse 

def blog_view(request):
    return render (request ,'blog/blog-home.html')
    
def blog_single(request):
    context = {'title':'Post one' , 'content':'this is a post one for this blog' , 'author':'amirabbas'}
    return render (request ,'blog/blog-single.html',context)
    pass
