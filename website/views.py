from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


def home(request):
    """Landing page: firm info sections + latest 3 posts."""
    latest_posts = Post.objects.filter(is_published=True)[:3]
    context = {"latest_posts": latest_posts}
    return render(request, "website/home.html", context)


def post_list(request):
    """Full, paginated list of published posts, with optional category filter."""
    posts = Post.objects.filter(is_published=True)

    category = request.GET.get("category")
    if category:
        posts = posts.filter(category=category)

    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "categories": Post.CATEGORY_CHOICES,
        "active_category": category,
    }
    return render(request, "website/post_list.html", context)


def post_detail(request, slug):
    """Single post page."""
    post = get_object_or_404(Post, slug=slug, is_published=True)
    related_posts = (
        Post.objects.filter(is_published=True, category=post.category)
        .exclude(pk=post.pk)[:3]
    )
    context = {"post": post, "related_posts": related_posts}
    return render(request, "website/post_detail.html", context)
