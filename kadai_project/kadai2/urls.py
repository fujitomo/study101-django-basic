from django.urls import path
from .views import CharactorCreaterView, CharactorListView

urlpatterns = [
    path('create/', CharactorCreaterView.as_view(), name='create'),
    path('list/', CharactorListView.as_view(), name='list'),
]
