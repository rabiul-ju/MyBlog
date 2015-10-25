from django.views.generic.list import ListView
from django.shortcuts import render

# Create your views here.
from .models import MyBlog


class ShowBlogListView(ListView):
    model = MyBlog
    template_name = 'show_blog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_list = context['object_list']
        page = int(self.request.GET.get('page')) - 1 if self.request.GET.get('page') else None
        if page and page > 0:
            context['object_list'] = blog_list[page * 6 - 1: page * 6 + 6]
        else:
            context['object_list'] = blog_list[0:6]

        pagination = list()
        for i in range(int(blog_list.count() / 6) + 1):
            pagination.append(i + 1)
        context['pagination'] = pagination
        return context
