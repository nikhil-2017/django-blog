from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post, imgPost, Question, QAnswer
from django.db.models import Q
from django.views.generic import (
    TemplateView,
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
def home(request):
    context ={
            'posts' : Post.objects.all()
        }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def imghome(request):
    contexts ={
            'imgposts' : imgPost.objects.all()
        }
    return render(request,'blog/imghome.html',contexts)

class imgPostListView(ListView):
    model = imgPost
    template_name = 'blog/imghome.html'
    context_object_name = 'imgposts'
    ordering = ['-date_posted'] 
    paginate_by = 2

class UserimgPostListView(ListView):
    model = imgPost
    template_name = 'blog/user_imgposts.html'
    context_object_name = 'imgposts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return imgPost.objects.filter(author=user).order_by('-date_posted')


class imgPostDetailView(DetailView):
    model = imgPost


class imgPostCreateView(LoginRequiredMixin , CreateView):
    model = imgPost
    fields = ['title', 'img', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


class imgPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = imgPost
    fields = ['title', 'img', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        imgpost = self.get_object()
        if self.request.user == imgpost.author:
            return True
        return False


class imgPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = imgPost
    success_url = '/imghome/'

    def test_func(self):
        imgpost = self.get_object()
        if self.request.user == imgpost.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html')

class SearchResultsView(ListView):
    model = [Post]
    template_name = 'blog/search_results.html'
    ordering = ['-date_posted'] 

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query)
        ).order_by('-date_posted')

        return object_list

def queshome(request):
    context ={
            'questions' : Question.objects.all()
        }
    return render(request,'blog/queshome.html',context)

class QuesListView(ListView):
    model = Question
    template_name = 'blog/queshome.html'
    context_object_name = 'questions'
    #context_object_name2 = 'qans'
    ordering = ['-date_posted'] 
    paginate_by = 2

class UserQuesListView(ListView):
    model = Question
    template_name = 'blog/user_ques.html'
    context_object_name = 'questions'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(author=user).order_by('-date_posted')

class QuesDetailView(DetailView):
    model = {
        "Question":Question, 
        "QAnswer":QAnswer
    }


class QAnsDetail(ListView):
    model = QAnswer
    template_name = 'blog/search_results.html'
    ordering = ['-date_posted'] 

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = QAnswer.objects.filter(
            Q(question__question__icontains=query) | Q(author__username__icontains=query) | Q(answer__icontains=query)
        ).order_by('-date_posted')

        return object_list

class QuesCreateView(LoginRequiredMixin ,CreateView):
    model = Question
    fields = ['question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class QuesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class QuesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/queshome/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class QAnsCreateView(LoginRequiredMixin ,CreateView):
    model = QAnswer
    fields = ['question','answer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QAnsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = QAnswer
    fields = ['question', 'answer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.author:
            return True
        return False


class QAnsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = QAnswer
    success_url = '/queshome/'

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.author:
            return True
        return False