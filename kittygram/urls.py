from django.urls import include, path

from cats.views import APICat, cat_detail, hello

urlpatterns = [
   # Исправил код,
   # ведь синтаксис вызова view-классов отличается
   # от синтаксиса вызова view-функций.
   path('cats/', APICat.as_view()),
   path('hello/', hello),
   path('cats/<int:pk>/', cat_detail),
]
