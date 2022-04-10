from django.urls import include, path

from cats.views import cat_list, cat_detail, hello

urlpatterns = [
   path('cats/', cat_list),
   path('hello/', hello),
   path('cats/<int:pk>/', cat_detail),
]
