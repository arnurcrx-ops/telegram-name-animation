FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование скрипта
COPY telegram_bio_animation.py .

# Переменные окружения (будут установлены в Railway/Render)
ENV API_ID=""
ENV API_HASH=""
ENV PHONE=""

# Запуск бота
CMD ["python", "telegram_bio_animation.py"]
