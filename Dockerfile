FROM python:3.11.2-slim-bullseye

WORKDIR /app

COPY . /app

WORKDIR /app/simplemortgage

RUN pip install --no-cache-dir -r /app/requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]