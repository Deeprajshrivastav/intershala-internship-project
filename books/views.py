from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView
from .filters import orderFilter
from django.contrib import messages
# Create your views here.


def home(request):
    myFilter = orderFilter(request.GET, queryset=Post.objects.all())
    myFilter.labels = ['Filter by Genre', 'Filter by language']
    post = myFilter.qs
    context = {
        'posts': post,
        'myFilter': myFilter
    }
    return render(request, 'books/index.html', context)


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'genre', 'language', 'info']
    template_name = 'books/post_form.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, "Post Created Successfully")
        return super().form_valid(form)