from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single(request):
    # اضافه کردن تگ و تاریخ به context
    context = {
        'title': 'Post one',
        'content': 'this is a post one for this blog',
        'author': 'amirabbas',
        'published_date': '1403/12/12',
        'tags': ['marketing'],  # تگ‌ها
    }
    return render(request, 'blog/blog-single.html', context)
