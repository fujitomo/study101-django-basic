from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kadai1.urls')),
    path('', include('kadai2.urls')),

]
