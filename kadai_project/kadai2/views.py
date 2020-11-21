from .models import KimetsuCharactorModel
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import KimetsuCharactorForm


class CharactorCreaterView(CreateView):
    """鬼滅の刃キャラクター登録View"""
    model = KimetsuCharactorModel
    form_class = KimetsuCharactorForm
    template_name = 'create.html'
    success_url = reverse_lazy('list')


class CharactorListView(ListView):
    """鬼滅の刃キャラクター一覧View"""
    template_name = 'list.html'

    def get_queryset(self):
        return KimetsuCharactorModel.objects.all()
