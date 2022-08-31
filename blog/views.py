from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

#.当前目录 models.py和views.py在同一目录下
# Create your views here.

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
#return render 方法渲染模板 blog/post_list.html 得到结果

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
