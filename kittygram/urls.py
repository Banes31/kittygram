from django.urls import include, path

from cats.views import cat_list
from cats.views import hello

urlpatterns = [
   path('cats/', cat_list),
   path('hello/', hello),
]
