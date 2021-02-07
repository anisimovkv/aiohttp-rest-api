## Реализовано Rest Api

* get_list - возврат всех данных
* pages постраничное перемещение и доступ к элементам
* set_data добавление сущности
* delete удаление сущности
* login доступ по учетной записи.

### Установка
```bash
pip install -r requirements.txt
```

### Запуск
```bash
python app.py --host 127.0.0.1 --port 4000
```

### Docker 
1. Построение образа
```bash
docker build -t aiohttp-test .
```
2. Запуск контейнера
```bash
docker run --name server-aiohttp -p 4000:4000 -d --rm aiohttp-test
```

### Swagger
```bash
http://127.0.0.1:4000/api/v1/doc
```

> ### Примичание:
> на представления set_data, delete, применен декаратор login_required, поэтому эти функции не отображаются в swagger.

## Инструкция

### 1. Получить все данные:

```bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.1:4000/api/v1/get_list/
```

### 2. Постраничное представление

```bash
 curl -X GET http://127.0.0.1:4000/api/v1/pages?page=2
 ```

#### Результат:

```bash
{"data": {"superhero": "Superman", "publisher": "DC Comics", "alter_ego": "Kal-El", "first_appearance": "Action Comics #1", "characters": "Kal-El"}, "links":
{"self": "http://127.0.0.1:4000/api/v1/pages?page=2",
 "first": "http://127.0.0.1:4000/api/v1/pages?page=1",
"last": "http://127.0.0.1:4000/api/v1/pages?page=20",
"privies": "http://127.0.0.1:4000/api/v1/pages?page=1",
 "next": "http://127.0.0.1:4000/api/v1/pages?page=3"}}
```

### 3. Логин

```bash
curl -d '{"username":"flash", "password":"123"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:4000/api/v1/users/login/
```

### Результат:

```bash
{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.v2rsRY_ZTvciT94RuaiYpz_fGgaqTcS0U39UuYuQTQg"}
```

### 4. Установка нового значения, возможна только при получении токена и указания имени.
 - поля:
```bash
-H "user: flash"
-H "Authorization: Bearer
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.v2rsRY_ZTvciT94RuaiYpz_fGgaqTcS0U39UuYuQTQg"
```
#### Запрос:
```bash
curl -X POST http://127.0.0.1:4000/api/v1/set_data/ -H "user: flash" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.v2rsRY_ZTvciT94RuaiYpz_fGgaqTcS0U39UuYuQTQg" -H "Content-Type: application/json" -d "{\"key1\":\"value1\", \"key2\":\"value2\"}"

```

### 5. Удаление 
#### Запрос:
```bash
curl -i -H "Accept: application/json" "user: batman" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.v2rsRY_ZTvciT94RuaiYpz_fGgaqTcS0U39UuYuQTQg" -H "Content-Type: application/json" -X DELETE http://127.0.0.1:4000/api/v1/delete/20/
```
#### Результат
```bash
{"object was deleted:": {"key1": "value1", "key2": "value2"}}
```