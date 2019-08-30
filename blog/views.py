from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,CreateView,DeleteView,DetailView,UpdateView)
from django.utils import timezone
from blog.models import Post,Comment
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from blog.forms import PostForm,CommentForm,SignupForm

# ____________________POSTS___________________#

class Home(TemplateView):
    template_name = 'blog/home.html'

class About(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(UserPassesTestMixin,CreateView):
    login_url = '/login/'  # Login is required for this view to access send them to one
    redirect_field_name = 'blog/post_detail.html'  # After Login, Just redirect them to the specific Post detail
    form_class = PostForm
    model = Post

    def test_func(self):
        return self.request.user.is_superuser


class PostUpdateView(UserPassesTestMixin,UpdateView):
    login_url = '/login/'  # Login is required for this view to access send them to one
    redirect_field_name = 'blog/post_detail.html'  # After Login, Just redirect them to the specific Post detail
    form_class = PostForm
    model = Post

    def test_func(self):
        return self.request.user.is_superuser


class PostDeleteView(UserPassesTestMixin,DeleteView):
    login_url = '/login/'  # Login is required for this view to access send them to one
    redirect_field_name = 'blog/post_detail.html'  # After Login, Just redirect them to the specific Post detail
    success_url= reverse_lazy('post_list')  # provide View name; see home page url
    model = Post

    def test_func(self):
        return self.request.user.is_superuser


class DraftListView(UserPassesTestMixin,ListView):
    login_url = '/login/'  # Login is required for this view to access send them to one
    redirect_field_name = 'blog/post_list.html'  # After Login, Just redirect them to the specific Post detail
    model= Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

    def test_func(self):
        return self.request.user.is_superuser

    #makes the drafts page visible only to author

#_____________HERE COMES THE COMMENT SECTION_____________#


#  So this function works in 2 parts. One is before submit button and other is after submit
#  Before submit or pressing "comment" button on the post, a form is presented to user by default
#  After pressing submit, the form is processed. That is why there is first if/else condition.
@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)  # User click on a Post to comment, it sends a <pk> and it is used here
                                        # for redirection

    if request.method=='POST':  # if user filled the form and hit Enter/Submit
        form=CommentForm(request.POST)  # Get the values of Comment entered by user inside form object
        if form.is_valid():
            comment=form.save(commit=False)  # get the values inside comment object
            comment.post=post  # Connect the comment to Post object
            comment.author=request.user.username #passes the current user's username as comment's author
            comment.save()  # save comment into DB that is related to a particular Post via ForeignKey
            return redirect('post_detail',pk=post.pk)
            # if form is valid, post the comment the comment to the Post and redirect user to the specific post in
            # the blog he commented on. 'post_detail' is URL name
    else:
        form=CommentForm()  # if method!=Post, present a form to fill i.e comment page
    return render(request,'blog/comment_form.html',{'form':form})  # render actual page to display in any case

@login_required
def comment_update(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data['text']
            comment.text=text
            comment.approved_comment=False
            comment.update_comment()
            post_pk=comment.post.pk
            return redirect('post_detail',pk=post_pk)
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required  #add ne feature that it can be deleted by either the owner of blog or the actual commentator
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk  #after deletion it'll go using this pk because comment will be deleted so no <pk>
    comment.delete()  # delete from DB. Defined in models
    return redirect('post_detail',pk=post_pk)


@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()  # See the models file. It is a function defined there to set the value to true
    return redirect('post_detail',pk=comment.post.pk)  # it is the URL not template/HTML page
                                                       # comment is related to a post which has a pk

def comment_approve_edit(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve_edit()  # See the models file. It is a function defined there to set the value to true
    return redirect('post_detail',pk=comment.post.pk)  # it is the URL not template/HTML page
                                                       # comment is related to a post which has a pk

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()  #method in models
    return redirect('post_detail',pk=pk)


####################### Signup#########
# Let's see the basic UsercreationView with function based view

def signup(request):
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form =SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = SignupForm()
        #form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})

 # It is working so let us move on to second part. This is very basic requires no models and provides 2 password matches
#########################################
#For second method, Go to forms.py and createa form there first
# Done with that? Now import the Signup Form from the forms.py and change the 3rd line of  signup method




















