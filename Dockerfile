FROM python:3.10-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN ~/.local/bin/poetry config virtualenvs.create false
RUN ~/.local/bin/poetry install


FROM python:3.10-slim

RUN useradd -m -r -u 1000 botuser
RUN apt-get update && apt-get install -y \
    ffmpeg \
    flac \
    libportaudio2 \
    libpulse0 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY . .

ENV PYTHONPATH=/app
ENV GRACE_SERVICE_URL=""
ENV TELEGRAM_TOKEN=""

RUN chown -R botuser:botuser /app
RUN mkdir -p /app/temp && chown -R botuser:botuser /app/temp

USER botuser

CMD ["python", "app/__main__.py"]