from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Review
from .forms import ReviewForm
from .game_utils import get_game_id, get_game_trailer, get_game_detail, get_game_image

class ReviewListView(ListView):
    model = Review

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