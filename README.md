# project_de_el
loading data from an API into PostgreSQL

Скрипт забирает данные из [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts), сохраняет их в CSV, читает обратно и загружает в PostgreSQL. Повторный запуск безопасен: дубли не создаются благодаря ON CONFLICT (id) DO NOTHING.

## Задачи
1) Сбор данных из API
2) Получение списка словарей из ответа API
3) Преобразование в DataFrame
4) Сохранение DataFrame в CSV-файл
5) Чтение файла и загрузка данных из CSV в список кортежей
6) Подключение к бд PostgreSQL
7) Создание таблицы
8) Загрузка данных в таблицу

## Структура проекта
```text
.
├── extract.py          # получение данных из API и сохранение в CSV
├── read_csv.py         # чтение CSV и преобразование в список кортежей
├── load.py             # подключение к PostgreSQL, создание таблицы, вставка
├── .env.example        # шаблон переменных окружения (без секретов)
├── .gitignore          # исключает .env, venv, данные
├── requirements.txt    # зависимости проекта
```

## Установка и запуск
1) Клонировать репозиторий: git clone <url-репозитория>
2) Создать и активировать виртуальное окружение: 
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
3) Установить зависимости: 
```bash
pip install -r requirements.txt
```
4) Создать .env на основе .env.example и заполнить своими параметрами:
```bash
cp .env.example .env
```
Затем откройте .env и укажите:
```
DB_NAME=your_database
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```
5) Убедитесь, что у вас уже создана база данных
6) Запустить скрипт: 
```bash
python load.py
```

## Результат: Таблица raw_data со схемой
Колонка	 | Тип    |	Ограничение
"userId" | INTEGER|	
id	     | INTEGER| PRIMARY KEY
title	 |    TEXT|	
body	 |    TEXT|	

Скрипт загружает данные в таблицу raw_data. Проверено: после первого запуска в таблице 100 строк, после повторного — те же 100 без дублей.
Вывод, где 100 - количество строк в списке, 2 строка - первый кортеж с данными, 100 - сколько строк в таблице:
```
100
(1, 1, 'sunt aut facere...', 'quia et suscipit...')
100
```

## Используемые библиотеки
requests, pandas, psycopg2-binary, python-dotenv

## Функции
1) extract() - получает данные из API и преобразует в DataFrame
2) save_to_csv() - сохраняет DataFrame в csv файл
3) read_csv_to_tuples() - считывает csv файл и сохраняет кортежи в список

## Лицензия
MIT