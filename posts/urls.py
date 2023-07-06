from django.urls import path
from .views import post_create_form_view, post_list_view
app_name='posts'

urlpatterns = [
    path('', post_list_view, name='post-list'), # posts 전체 보기
    path('create/',post_create_form_view, name='post-create'),
]
