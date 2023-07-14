FROM python:3.8

COPY . /app
RUN pip install poetry
WORKDIR /app
RUN poetry install --no-dev

CMD ["poetry", "run", "start-game"]
