from django.urls import path

from . import views
from .views import HomeView, ArticleDetail, AddPostView, EditPostView, DeletePostView, CategoryView, LikeView

urlpatterns = [
    #path('',views.homepage, name = 'home'),
    path('', HomeView.as_view(), name= "home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name= "detailed_view"),
    path('add_post/', AddPostView.as_view(), name= "add_post"),
    path('article/edit/<int:pk>',EditPostView.as_view(), name = "edit_post" ),
    path('article/delete/<int:pk>',DeletePostView.as_view(), name = "delete_post"),
    path('category/<str:cats>/',CategoryView, name= "category"),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    
    ]


