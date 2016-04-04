from django import forms
from .models import Post
from .forms import BlogPostForm

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content','image')
    def new_post(request):
    form = BlogPostForm(request.POST, request.FILES)
    return render(request, 'blogpostform.html', {'form': form})