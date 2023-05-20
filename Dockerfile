FROM python:3.11.1-alpine
LABEL maintainer="oithegod@icloud.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.py /usr/local/bin/entrypoint.py
RUN chmod +x /usr/local/bin/entrypoint.py

COPY . .

RUN mkdir -p /vol/web/media

RUN chmod -R 755 /vol/web

ENTRYPOINT ["python", "/usr/local/bin/entrypoint.py"]
