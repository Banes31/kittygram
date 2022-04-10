from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cat
from .serializers import CatSerializer


# view-функцию cat_list заменили на view-класс APICat.
# @api_view(['GET', 'POST'])
# def cat_list(request):
#     """В случае POST-запроса создается объект класса Cat.
#     В случае GET-запроса возвращается информация о всех объектах класса Cat.
#     """
#     if request.method == 'POST':
#         # Создаём объект сериализатора
#         # и передаём в него данные из POST-запроса
#         serializer = CatSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             # Если полученные данные валидны —
#             # сохраняем данные в базу через save().
#             serializer.save()
#             # Возвращаем JSON со всеми данными нового объекта
#             # и статус-код 201
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # Если данные не прошли валидацию —
#         # возвращаем информацию об ошибках и соответствующий статус-код:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)

class APICat(APIView):
    """В случае POST-запроса создается объект класса Cat.
    В случае GET-запроса возвращается информация о всех объектах класса Cat.
    """
    def get(self, request):
        """В случае GET-запроса возвращается нижеуказанная информация.
        О всех объектах класса Cat.
        """
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        """В случае POST-запроса создается объект класса Cat."""
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])  # Применили декоратор и указали разрешённые методы
def hello(request):
    """Тестовая функция для проверки алгоритма работы с POST/GET-запросами."""
    # По задумке, в ответ на POST-запрос нужно вернуть JSON с теми данными,
    # которые получены в запросе.
    # Для этого в объект Response() передаём словарь request.data.
    if request.method == 'POST':
        return Response({'message': 'Получены данные', 'data': request.data})

    # В ответ на GET-запрос нужно вернуть JSON
    # Он тоже будет создан из словаря, переданного в Response()
    return Response({'message': 'Это был GET-запрос!'})


@api_view(['PUT', 'PATCH', 'DELETE'])
def cat_detail(request, pk):
    """В случае PUT/PATCH-запроса изменяется объект класса Cat=pk.
    В случае DELETE-запроса удаляется объект класса Cat=pk.
    """
    cat = Cat.objects.get(id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            cat.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = CatSerializer(cat, many=False, partial=True)
    return Response(serializer.data)
