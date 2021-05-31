from django.urls import path

from . import views
from .views import HomeView, ArticleDetail, AddPostView, EditPostView, DeletePostView, LikeView, ShowProfileView, EditProfilePageView, AddCommentView
from CVGEN.views import AddEducationView, AddExperienceView, AddSkillsView
from register.views import CreateProfilePageView

urlpatterns = [ 
    path('', HomeView.as_view(), name= "home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name= "detailed_view"),
    path('add_post/', AddPostView.as_view(), name= "add_post"),
    path('article/edit/<int:pk>',EditPostView.as_view(), name = "edit_post" ),
    path('article/delete/<int:pk>',DeletePostView.as_view(), name = "delete_post"),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('<int:pk>/profile/',ShowProfileView.as_view(), name = 'profile'),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(), name = 'edit_profile_page'),
    path('<int:pk>/edit_profile_page/add_education/',AddEducationView.as_view(), name = 'add_education'),
    path('<int:pk>/edit_profile_page/add_experience/',AddExperienceView.as_view(), name = 'add_experience'),
    path('<int:pk>/edit_profile_page/add_skills/',AddSkillsView.as_view(), name = 'add_skills'),
    path('create_profile_page/',CreateProfilePageView.as_view(), name = 'create_profile_page'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name ="add_comment"),
    
    ]


