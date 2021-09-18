FROM python:3.7.9

WORKDIR /var/mapublico

COPY . .

RUN apt -y update
RUN apt -y install wget tar libgtk-3-dev libdbus-glib-1-dev
RUN python -m pip install --upgrade pip

# Instalación de paquetes
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Lanzar API
CMD flask run -p 8080 -h 0.0.0.0
