FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add curl

RUN adduser -S -u 1000 -h /app -H python
RUN chown 1000:1000 . -R
USER 1000:1000

COPY requirements.txt .
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://127.0.0.1:8000/health || exit 1

CMD ["/app/.local/bin/gunicorn", "--bind", "0.0.0.0:8000", "mravatar:app"]