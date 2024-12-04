FROM python:3.10-slim

# Diretório dentro do container
WORKDIR /app 

COPY ./PROJETO_PETCARE-main/requirements.txt /app/

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

COPY ./PROJETO_PETCARE-main /app/

WORKDIR /app/backend
RUN python manage.py migrate && \
    python manage.py loaddata surgery_fixture.json && \
    python manage.py loaddata gender_fixture.json && \
    python manage.py loaddata medicine_type_fixture.json && \
    python manage.py loaddata illness_status_fixture.json

EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
