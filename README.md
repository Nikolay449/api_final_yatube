## README.md

API для Yatube учебный проект для реализации социальной сети.

### Как запустить проект «API для Yatube»:

### Клонировать репозиторий и перейти в него в командной строке:

        git clone git@github.com:Nikolay449/api_final_yatube.git

### Cоздать и активировать виртуальное окружение:

        python3 -m venv venv

        source venv/bin/activate

### Установить зависимости из файла requirements.txt:

         python3 -m pip install --upgrade pip

         pip install -r requirements.txt

### Выполнить миграции:

         python3 manage.py migrate

### Запустить проект:

         python3 manage.py runserver
         
### Примеры работы с API:
#### для неавторизованных пользователей работа с API доступна в режиме чтения:

GET `api/v1/posts/` - получить список всех публикаций.  
При указании параметров limit и offset выдача должна работать с пагинацией  
GET `api/v1/posts/{id}/` - получение публикации по id  
GET `api/v1/groups/` - получение списка доступных сообществ  
GET `api/v1/groups/{id}/` - получение информации о сообществе по id  
GET `api/v1/{post_id}/comments/` - получение всех комментариев к публикации  
GET `api/v1/{post_id}/comments/{id}/` - Получение комментария к публикации по id  

#### для авторизованных пользователей пример работы с API:
Cоздания публикации:  
POST `/api/v1/posts/`  
в body  
  
    {
    "text": "string",
    "image": "string",
    "group": 0
    }
