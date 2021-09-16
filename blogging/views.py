from blogging.models import Post
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    model = Post
    queryset = Post.objects.exclude(published_date=None).order_by('-created_date')
    template_name = 'blogging/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        context = {'object': post}
        return render(request, 'blogging/detail.html', context)
