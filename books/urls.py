
from django.urls import path
from .views import PostCreateView, home

urlpatterns = [
    path('', home, name='home'),
    path('post/new/', PostCreateView.as_view(), name='add-book'),

]

