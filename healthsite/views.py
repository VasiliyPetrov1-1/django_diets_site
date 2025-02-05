from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'healthsite/post_list.html', {'posts': posts, 'is_diet_page': False})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'healthsite/post_detail.html', {'post': post, 'is_diet_page': True})
