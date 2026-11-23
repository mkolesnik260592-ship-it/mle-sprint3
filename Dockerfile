FROM python:3.11-slim

LABEL author=${AUTHOR}

COPY . ./churn_app

WORKDIR churn_app

RUN ["pip3", "install","--default-timeout=100", "--no-cache-dir", "-r", "requirements.txt"]

EXPOSE ${APP_PORT}

VOLUME /models

CMD uvicorn app.churn_app:app --reload --port ${APP_PORT} --host 0.0.0.0
