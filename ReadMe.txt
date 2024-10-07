ФСТР — организация, занимающаяся развитием и
популяризацией спортивного туризма в России и
руководящая проведением всероссийских соревнований в этом виде спорта.


-Клонирование проекта: git clone https://github.com/danpilnet/Pereval.git


-Для корректрной работы необходимо выполнить:
1) Создание виртуального окружения: python -m venv venv
2) Активировать виртуальное окружение:venv/scripts/activate
3) Установить бибилотеки:
asgiref             3.8.1
Django              5.1.1
django-filter       24.3
djangorestframework 3.15.2
pip                 24.2
psycopg2            2.9.9
python-dotenv       1.0.1
setuptools          65.5.1
sqlparse            0.5.1
tzdata              2024.2
wheel               0.38.4


-Переменные окружения:

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('FSTR_DB_LOGIN'),
        'PASSWORD': os.getenv('FSTR_DB_PASS'),
        'HOST': os.getenv('FSTR_DB_HOST'),
        'PORT': os.getenv('FSTR_DB_PORT'),
    },
}


-Диеректорию pereval необходимо выбрать как корневую директорию проекта


-Перейти в директорию pereval: cd pereval


-Запустить проект: python manage.py runserver

