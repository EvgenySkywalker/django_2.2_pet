FROM python:3.8.10-buster

WORKDIR /usr/local/test-project/

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN cat /etc/*release

# System deps:
RUN apt-get update \
   && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    gettext-base \
    git \
    libpq-dev \
    wget \
  && pip install --upgrade pip \
  && pip install "setuptools" \
  && pip install "poetry" && poetry --version


COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .