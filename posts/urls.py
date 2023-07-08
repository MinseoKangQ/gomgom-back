from django.urls import path

from .views import post_create_form_view,post_list_view, post_detail_view, post_create_complete

app_name='posts'

urlpatterns = [
    path('',post_list_view,name='post-list-all'),
    path('create/',post_create_form_view, name='post-create'),
    path('complete/', post_create_complete, name='post-create-complete'),
    path('<int:id>/', post_detail_view, name='post-detail'),
]
