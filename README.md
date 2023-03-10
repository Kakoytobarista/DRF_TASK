<center> <h2>Тестовое задание DRF</h2></center>


## Вопросы:
1. Как правильно сохранять modified_by?
Пояснение: при создании записи в запросе приходит только value, но в БД нужно записать не только value, но и того пользователя, который сделал POST-запрос.
Подсказка: Модели и сериализатор остаются неизменными.

### Ссылка на решение в коде:
https://github.com/Kakoytobarista/DRF_TASK/blob/a929d62bc3fff3144f52bac8702c11d1e28bd0f2/drf_task/apps/api/views.py#L20-L21

____
2. Для создания Entity на вход POST API подаётся json вида
     {"data[value]": 10} Как исправить сериализатор так, чтобы он мог принять поле "data[value]" и сохранить 
его в поле value? Пояснение: Python не позволит написать в сериализаторе 
data[value] = IntegerField(...), но есть другое решение. Подсказка: Модели остаются неизменными

### Ссылка на решение в коде:
(https://github.com/Kakoytobarista/DRF_TASK/blob/a929d62bc3fff3144f52bac8702c11d1e28bd0f2/drf_task/apps/api/serializers.py#L12-L27)


____
3. Как вывести propertiesв формате {key:value, ...}, если мы заранее не знаем сколько и каких key может быть?
Пояснение: Иногда нужно вывести данные, когда имена полей заранее неизвестны. См. пример ниже. 
Не обращайте внимания на то, что value - строка, это 
всего лишь пример, как может выглядеть properties.

```
[ 
  {
    "value": "circle",
    "properties": {
      "center": "100, 100",
      "radius": "50"
    }
  },
  {
    "value": "line",
    "properties": {
      "start": "150, 50",
      "end": "50, 150"
    }
  },
  {
    "value": "Медведь",
    "properties": {
      "класс": "Млекопитающие"
    }
  },
  {
    "value": "rectangle",
    "properties": {
      "corner_1": "50, 50",
      "corner_2": "150, 150"
    }
  }
]
```

#### Ссылка на решение в коде: 
https://github.com/Kakoytobarista/DRF_TASK/blob/a929d62bc3fff3144f52bac8702c11d1e28bd0f2/drf_task/apps/api/serializers.py#L30-L35

____

### Как развернуть приложение:


1. Запусить shell файл:
```
./run.sh
```

* Swagger: http://0.0.0.0:8000/redoc/
* Api: http://0.0.0.0:8000/api/v1/

____
### Генерация тестовых данных:
Если хочется сгенерировать тестовые данные можно воспользоваться
модулем factory у приложения service. С объектов в этом модуле, можно
с помощтю метода create_batch({количество инстансов}) создавать тестовые данные.

____

<h2>Мысли по поводу каждого из заданий:</h2>

1. Метод 'perform_create()' хорошо подходит для добавления значения в поле, потому что он 
предоставляет больше гибкости и контроля над процессом добавления данных. В 
сериализаторе не стоит делать этого, потому что сериализатор предназначен 
для преобразования данных из одного формата в другой, а не для добавления данных в поле.

____


2. В голову сразу пришли две реализации:
Первая использовать метод 'to_internal_value()' (Реализация по ссылке в коде), 
а вторая это переопределить метод 'create()'.
```
def create(self, validated_data):
     value = self.context['request'].data.get('data[value]')
     validated_data['value'] = value if value is not None else validated_data['value']
     entity_serializer = EntitySerializer(data=validated_data)
     entity_serializer.is_valid(raise_exception=True)
     return Entity.objects.create(**validated_data)
```
Для меня было очевидным лучше использовать первую реализацию, потому что она 
более простая и понятная. Она использует метод to_internal_value() для преобразования 
данных из входного запроса в внутреннее представление, которое 
может быть использовано для создания модели. Вторая реализация использует метод create() для
получения данных из входного запроса и создания модели. Она более сложная и менее понятная.


____

3. Когда прочитал задание подумал про две реализации которые первые приходят в голову.
Первая это использовать SerializerMethodField (он реализован в коде), а вторая использовать
метод to_representation.
```
    def to_representation(self, instance):
        data = super().to_representation(instance)
        properties = instance.properties.all()
        data['properties'] = {prop.key: prop.value for prop in properties}
        return data
```
Обе реализации предоставляют простой и эффективный способ 
отображения данных без необходимости знать имена полей и их количество. 
Однако первая реализация более предпочтительна, поскольку 
она использует метод SerializerMethodField, который позволяет получить 
данные из модели и предоставить их в виде словаря. Вторая реализация 
использует метод to_representation, который предоставляет более гибкий 
подход для получения данных из модели, но менее эффективный.

____

