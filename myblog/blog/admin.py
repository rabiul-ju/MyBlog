from django.contrib import admin

# Register your models here.
from .models import MyBlog,Tag


class MyBlogAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]


admin.site.register(MyBlog, MyBlogAdmin)
admin.site.register(Tag)

