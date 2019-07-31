from  blog import views
from django.urls import path

#app_name='blog'  # if you declare app_name, you'll have to use it in templates
urlpatterns = [

    path('list/',views.PostListView.as_view(),name='post_list'),
    path('<int:pk>',views.PostDetailView.as_view(), name='post_detail'),
    path('new/',views.CreatePostView.as_view(),name='post_new'),
    path('<int:pk>/edit/',views.PostUpdateView.as_view(), name='edit_post'),
    path('<int:pk>/remove/',views.PostDeleteView.as_view(), name='delete_post'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('<int:pk>/comment/',views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('<int:pk>/publish/', views.post_publish, name='publish_post'),
    path('signup/',views.signup,name='signup')

]