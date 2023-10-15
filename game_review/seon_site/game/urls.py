from django.urls import path
from .views import (
    HomeListView,
    CommentView,
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
)

urlpatterns = [
    path('', HomeListView.as_view(template_name='home/index.html'), name='home-index'),
    path('add-comment/', CommentView.as_view(), name='add-comment'),
    path('reviews/', ReviewListView.as_view(template_name='game/review_list.html'), name='review-list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review-new'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]