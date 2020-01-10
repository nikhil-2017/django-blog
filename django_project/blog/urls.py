from django.contrib import admin
from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    imgPostListView,
    imgPostCreateView,
    imgPostDeleteView,
    imgPostDetailView,
    imgPostUpdateView,
    UserimgPostListView,
    SearchResultsView,
    QuesListView,
    UserQuesListView,
    QuesDetailView,
    QuesCreateView,
    QuesUpdateView,
    QuesDeleteView,
    QAnsCreateView,
    QAnsUpdateView,
    QAnsDeleteView,
    QAnsDetail
)
from . import views


urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('post/user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),

    path('imghome/',imgPostListView.as_view(),name='blog-imghome'),
    path('imghome/imgpost/user/<str:username>',UserimgPostListView.as_view(),name='user-imgposts'),
    path('imghome/imgpost/new/',imgPostCreateView.as_view(),name='imgpost-create'),
    path('imghome/imgpost/<int:pk>/',imgPostDetailView.as_view(),name='imgpost-detail'),
    path('imghome/imgpost/<int:pk>/update/',imgPostUpdateView.as_view(),name='imgpost-update'),
    path('imghome/imgpost/<int:pk>/delete/',imgPostDeleteView.as_view(),name='imgpost-delete'),
    path('about/',views.about,name='blog-about'),

    path('queshome/',views.queshome,name='queshome'),
    path('queshome/ques/user/<str:username>',UserQuesListView.as_view(),name='user-ques'),
    path('queshome/ques/new/',QuesCreateView.as_view(),name='ques-create'),
    path('queshome/ques/<int:pk>/',QuesDetailView.as_view(),name='ques-detail'),
    path('queshome/ques/<int:pk>/update/',QuesUpdateView.as_view(),name='ques-update'),
    path('queshome/ques/<int:pk>/delete/',QuesDeleteView.as_view(),name='ques-delete'),

    path('queshome/ans/new/',QAnsCreateView.as_view(),name='ans-create'),
    path('queshome/ans/<int:pk>/update/',QAnsUpdateView.as_view(),name='ans-update'),
    path('queshome/ans/<int:pk>/delete/',QAnsDeleteView.as_view(),name='ans-delete'),
    path('quesans/<int:pk>/', QAnsDetail.as_view(), name='quesans'),
]
