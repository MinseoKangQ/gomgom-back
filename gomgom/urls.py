from django.urls import path
from .views import ai_view, home_view

app_name='gomgom'

urlpatterns = [
    path('home/', home_view, name='home'),
    path('ai/', ai_view, name='ai'),
]
