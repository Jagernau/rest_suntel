FROM python:3.10-slim
# Database
ENV DB_HOST=${DB_HOST}

# Postgres
ENV POSTGRES_HOST=${DB_HOST}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB_NAME=${POSTGRES_DB_NAME}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_PORT=${POSTGRES_PORT}
COPY . /rest_suntel
WORKDIR /rest_suntel
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
