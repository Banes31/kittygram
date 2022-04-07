from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        # Создаём объект сериализатора
        # и передаём в него данные из POST-запроса
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            # Если полученные данные валидны —
            # сохраняем данные в базу через save().
            serializer.save()
            # Возвращаем JSON со всеми данными нового объекта
            # и статус-код 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Если данные не прошли валидацию —
        # возвращаем информацию об ошибках и соответствующий статус-код:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])  # Применили декоратор и указали разрешённые методы
def hello(request):
    # По задумке, в ответ на POST-запрос нужно вернуть JSON с теми данными,
    # которые получены в запросе.
    # Для этого в объект Response() передаём словарь request.data.
    if request.method == 'POST':
        return Response({'message': 'Получены данные', 'data': request.data})

    # В ответ на GET-запрос нужно вернуть JSON
    # Он тоже будет создан из словаря, переданного в Response()
    return Response({'message': 'Это был GET-запрос!'})
