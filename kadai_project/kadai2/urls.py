from django.urls import path
from .views import createView, listView

urlpatterns = [
    path('create/', createView, name='create'),
    path('list/', listView, name='create'),
]
