from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from .game_utils import get_game_id, get_game_trailer, get_game_detail, get_game_image

class HomeListView(ListView):
    model = Review
    template_name = 'home/index.html'
    context_object_name = 'review_data'

    def get_queryset(self):
        return Review.objects.order_by('-created_at')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = Comment.objects.order_by('-created_at')
        page_number = self.request.GET.get('page', 1)
        paginator = Paginator(comments, 3)
        comments_page = paginator.get_page(page_number)
        comment_form = CommentForm()

        review_data = []
        for review in context['review_data']:
            app_id = get_game_id(review.title)
            thumbnail_url = get_game_image(app_id)
            review_data.append({'review': review, 'thumbnail_url': thumbnail_url})

        context['review_data'] = review_data
        context['comments_page'] = comments_page
        context['comment_form'] = comment_form

        return context

class ReviewListView(ListView):
    model = Review
    template_name = 'game/review_list.html'
    context_object_name = 'review_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        review_data = []
        for review in context['review_data']:
            app_id = get_game_id(review.title)
            thumbnail_url = get_game_image(app_id)
            review_data.append({'review': review, 'thumbnail_url': thumbnail_url})

        context['review_data'] = review_data
        return context

class ReviewDetailView(DetailView):
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_id = get_game_id(self.object.title)
        context['trailer_url'] = get_game_trailer(app_id)
        context['detail_url'] = get_game_detail(app_id)
        context['thumnail_url'] = get_game_image(app_id)
        return context

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('review-list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name_suffix = '_confirm_update'
    success_url = reverse_lazy('review-list')

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('review-list')

class CommentView(View):
    template_name = 'home/index.html'
    comments_per_page = 3

    def get(self, request):
        comments = Comment.objects.order_by('-created_at')
        page_number = request.GET.get('page', 1)
        paginator = Paginator(comments, self.comments_per_page)
        comments_page = paginator.get_page(page_number)
        comment_form = CommentForm()

        return render(request, self.template_name, {'comments_page': comments_page, 'comment_form': comment_form})

    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
        
        return redirect('home-index')