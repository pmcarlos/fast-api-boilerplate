FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql python-psycopg2 postgresql-server-dev-all \
  && apt-get clean

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev

COPY . /code/

ENTRYPOINT ["sh", "/code/entrypoint.sh"]
