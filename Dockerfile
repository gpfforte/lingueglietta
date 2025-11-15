# Usa un'immagine Python ufficiale come immagine base
FROM python:3.13-slim-bookworm

# Imposta le variabili d'ambiente per Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Installa le dipendenze di sistema necessarie per psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia il file dei requisiti e installa le dipendenze
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice del progetto nella directory di lavoro
COPY . /app/

# Crea la directory per i log prima di eseguire comandi Django
RUN mkdir -p /app/logs

# Raccogli i file statici
RUN python manage.py collectstatic --noinput

# Esponi la porta su cui Gunicorn sarà in ascolto
EXPOSE 8000