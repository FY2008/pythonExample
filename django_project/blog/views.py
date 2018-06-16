from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.safestring import mark_safe

import mistune
import markdown

# 模型导入
from .models import Article


def site_home(request):
    """站点主页面"""
    return render(request, 'home/site_home.html', {})


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'


class ArticleDetailView(DetailView):
    """文章详情页

    """
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    # pk_url_kwarg 用于接受来自url中的参数作为主键
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.views += 1
        obj.save()
        return obj
