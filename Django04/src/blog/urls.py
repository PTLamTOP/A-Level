"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from myapp.views import index
from myapp.views import ArticleListView, CustomLoginView, \
    CustomLogoutView, SearchResultList, RegistrationView, ChangingPasswordView, \
    ArticleDetailView, CreateCommentView, UpdateCommentVIew, DeleteCommentView, \
    CommentDetailView, UpdateCommentStatusVIew, ArticleCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view(), name='index'),
    # path('', index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('search/', SearchResultList.as_view(), name='search'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('pass-change/', ChangingPasswordView.as_view(), name='pass-change'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('comment-create/>', CreateCommentView.as_view(), name='comment-create'),
    path('comment-update/<int:pk>', UpdateCommentVIew.as_view(), name='comment-update'),
    path('comment-update-status/<int:pk>', UpdateCommentStatusVIew.as_view(), name='comment-update-status'),
    path('comment-delete/<int:pk>', DeleteCommentView.as_view(), name='comment-delete'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
    path('article-create/', ArticleCreateView.as_view(), name='article-create'),
]
