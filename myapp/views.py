from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Profile, Comment, Experience, Education, KeySkill
from . forms import PostForm, EditForm




class HomeView(ListView):
    model = Post
    template_name  = "home.html"
    ordering = ['-pub_date']

   
    
    
class ArticleDetail(DetailView):
    model = Post
    template_name = "detailed_view.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_query = get_object_or_404(Post, id = self.kwargs['pk'])
        liked = False
        if like_query.likes.filter(id= self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    
    
class AddCommentView(CreateView):
    model = Comment
    template_name = "add_comment.html"
    fields = ['name', 'body',]
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context['page_user'] = page_user
        return context
        
    
class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "edit_post.html"
    
   
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
    
   


def LikeView(request, pk):
    post = get_object_or_404(Post, id= request.POST.get("post_id"))
    #liked= False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        #liked = False  
    else:
        post.likes.add(request.user)
        #liked = True
    return HttpResponseRedirect(reverse('detailed_view', args=[str(pk)]))


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website', 'facebook', 'linkedin', 'instagram', 'twitter', 'github', 'phone']
    success_url = reverse_lazy('home')
    

    
    


    

