# Публикуем фотографии в телграм. 
## Описание
Этот проект сделан для того, чтобы автоматизировать сбор фотографий космоса и их публикации в Telegram.
## Установка
Скачайте необходиые файлы, затем используйте `pip`(или `pip3`, если есть конфликты с Python2) для установки зависимостей. Зависимости можно установить командой, представленной ниже. Создайте бота у отца ботов. Создайте новый канал Telegram.

Установите зависимости командой:

`pip install -r requirements.txt`

## Пример запуска из скрипта
Для запуска скрипта у вас уже должен быть установлен Pythn3.

Для получения необходмых изображенй необходимо написать:

`python main.py`

## Переменные окружения 
Часть настроек проекта берется из переменных окружения. Переменные окружения - это переменные, значения которых присваиваются программе Python извне. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: Переменная = значение.
Пример содержания `.env`:

`NASA_KEY = 'nasa_key'`

`TG_TOKEN = 'tg_token'`

Получить токен `NASA_KEY` можно на сайте [NASA](https://api.nasa.gov/#epic). Получить токен `TG_TOKEN` можно у отца ботов.