# REST Фото менеджер

Сервис Api управления фотографиями. 

Разработан на python с:
* Django REST framework.

## Описание функционала:

1. Загрузка фотографий авторизованным пользователям с возможностью указывать различную метадату: геолокацию, описание, имена людей на фото.

2. Вывод списка фотографий, без мета данных с возможностью фильтровать по 

** дате;

** геолокации;

** имени человека на фото.

3. Вывод информации и метаданных фотографии по айди;

4. Апи автодополнение по поиску возможных имен людей, присутствующих на фотографиях. 


## Установка и запуск

1. Внутри директории проекта активировать виртуальное окружение (venv/ — название виртуального окружения)
````
python -m venv venv
venv/bin/activate
````
2.Склонировать репозиторий с Github.com:
````
git clone https://github.com/Povarenskiy/rest_photo_manager.git
```` 
3. Установить зависимости
````
pip install -r requirements.txt
````
4. Применить миграции
````
python manage.py makemigrations
python manage.py migrate
````
5. Запустить сервер
````
python manage.py runserver
````
6. В браузере перейти на localhost порт 8000
````
http://127.0.0.1:8000/
````

## Панель администратора
1. Создать аккаунт администратора  
````
python manage.py createsuperuser
````
2. В браузере зайти в панель администратора
````
http://127.0.0.1:8000/admin/
````

## Тесты 
1. В директории проекта
````
python manage.py test mailing_app
````

## Api

### Cпецификация
````
http://127.0.0.1:8000/swagger/
```` 
### Сервис

Фотографии: ````/api/photo/```` 
* получить список
* добавить новую


Фотография с id: ````/api/photo/<pk>/````
* получить/обновить атрибуты
* удалить


Имена ````/api/name/```` 
* получить список 
* добавить новое 


Имя c id ````/api/name/<pk>/````
* получить/обновить атрибуты
* удалить 

