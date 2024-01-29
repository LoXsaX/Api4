# Публикуем фотографии в телграм. 
## Описание
Этот проект сделан для того, чтобы автоматизировать сбор фотографий космоса и их публикации в Telegram.
## Установка
Скачайте необходиые файлы, затем используйте `pip`(или `pip3`, если есть конфликты с Python2) для установки зависимостей. Зависимости можно установить командой, представленной ниже. Создайте бота у отца ботов. Создайте новый канал Telegram.

Установите зависимости командой:

`pip install -r requirements.txt`

## Пример запуска из скрипта
Для запуска скрипта у вас уже должен быть установлен Pythn3.

Для публикации необходмых изображенй необходимо написать:
`python upload_telegram.py`

Пример скачивани картинок для nasa_apod:
`python fetch_nasa_apod.py `

Пример скачивани картинок для nasa_epic:
`python get_epic_photo.py`

Пример скачивани картинок для space_x:
`python space_x.py`

## Переменные окружения 
Часть настроек проекта берется из переменных окружения. Переменные окружения - это переменные, значения которых присваиваются программе Python извне. Чтобы их определить, создайте файл `.env` рядом с `upload_telegram.py` и запишите туда данные в таком формате: Переменная = значение.
Пример содержания `.env`:

`NASA_KEY = 'nasa_key'`

`TG_TOKEN = 'tg_token'`

`TG_CHAT_ID = 'chat_id'` 

Получить токен `NASA_KEY` можно на сайте [NASA](https://api.nasa.gov/#epic). Получить токен `TG_TOKEN` можно у отца ботов.
