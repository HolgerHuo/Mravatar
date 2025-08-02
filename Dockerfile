FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=5m --timeout=3s \
  CMD wget --no-verbose http://[::1]:8000/health --spider || exit 1

ENTRYPOINT ["/usr/local/bin/gunicorn"]
CMD ["--bind", "[::]:8000", "mravatar:app"]
