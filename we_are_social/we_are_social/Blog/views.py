import django
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(-published_date)
    return render(request, "blogtests.html", {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog/postdetail.html", {'post': post})
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0) # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1  # clock up the number of post views
    post.save()
    return render(request, "blog/postdetail.html", {'post': post})


def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = PostForm()
    return render(request, 'blogpostform.html', {'form': form})
