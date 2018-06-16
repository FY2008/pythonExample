from django.urls import path
from . import views as blog_views
app_name = 'blog'
urlpatterns = [
    path('', blog_views.IndexView.as_view(), name='index'),
    path(
        'p/<int:article_id>',
        blog_views.ArticleDetailView.as_view(),
        name='detail'),
]
