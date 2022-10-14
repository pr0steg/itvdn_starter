from django.urls import path
from lesson_3 import views
from lesson_3.post_view import MyTemplateView, post_page
# from lesson_3.post_view import post_page, index_post

urlpatterns = [
    path('main/', views.main),
    path('main/text/', views.text, name="text"),
    path('main/file/', views.file, name="file"),
    path('main/redirect/', views.redirect, name="redirect"),
    path('main/not-allowed/', views.not_allowed, name="not_allowed"),
    path('main/json/', views.json, name="json"),

    path('class-view/', views.MyView.as_view(), name='class_view'),

    # path('post/', index_post, name='post'),
    path('post/', MyTemplateView.as_view(), name='post'),
    path('post/<int:number>/', post_page, name='post_list'),
]
