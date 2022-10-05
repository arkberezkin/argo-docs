FROM python:3.9.5-slim-buster

# RUN adduser --system --disabled-password --uid 10000 --group --gecos '' docker-user
# RUN mkdir /app && chown docker-user:docker-user /app
# USER docker-user

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY src src

CMD python3 src/main.py
