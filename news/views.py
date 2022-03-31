from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'
    ordering = ['time_create']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        return context


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    form_class = PostForm
    context_object_name = 'post'
    queryset = Post.objects.order_by('time_create')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['category'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'post_create.html'
    permission_required = ('news.add_post',)
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    permission_required = ('news.change_post',)
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    permission_required = ('news.delete_post',)
    queryset = Post.objects.all()
    success_url = '/news/'
