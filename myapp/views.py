from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post, Category
from . forms import PostForm, EditForm




class HomeView(ListView):
    model = Post
    template_name  = "home.html"
    ordering = ['-pub_date']
    
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(HomeView ,self).get_context_data(*args,**kwargs)
    #     context['cat_menu'] = cat_menu
    #     return context
     
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    
class ArticleDetail(DetailView):
    model = Post
    template_name = "detailed_view.html"
    
    
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        
        like_query = get_object_or_404(Post, id = self.kwargs['pk'])
        liked = False
        if like_query.likes.filter(id= self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        # total_likes = like_query.total_likes()
        # context["total_likes"] = total_likes
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    
class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "edit_post.html"
    
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
def CategoryView(request, cats):
    category_post = Post.objects.filter(category = cats)
    return render(request, 'category.html', {'cats':cats.title(), 'category_post': category_post} )

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
    
    


    

