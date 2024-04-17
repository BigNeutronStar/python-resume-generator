# Используем официальный образ Python 3.11 в качестве базового образа
FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы из локальной директории внутрь контейнера в директорию /app
COPY resume_manipulator.py .
COPY main.py .
COPY .env .
COPY requirements.txt .
COPY templates /app/templates

# Устанавливаем зависимости Python из файла requirements.txt без кеширования
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем команду по умолчанию, которая будет запускать приложение Python при запуске контейнера
CMD ["python", "main.py"]