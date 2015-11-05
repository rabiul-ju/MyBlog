from multiprocessing.sharedctypes import template

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.list import ListView
from blog.models import MyBlog
from blog.views import ShowBlogListView

urlpatterns = [
    # Examples:
    # url(r'^$', ListView.as_view(model= myblog,template_name = "home.html"), ),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ShowBlogListView.as_view(), name='show_blog_list'),
    url(r'^admin/', include(admin.site.urls)),
]

