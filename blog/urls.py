from django.urls import path
#from . import views
from .views import PostView, PostDetailView, AboutView

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', PostView.as_view(), name='post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('about', AboutView.as_view(), name='about'),
]