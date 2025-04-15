FROM python

WORKDIR usr/src/app

ENV PATH="/root/.local/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3

COPY pyproject.toml poetry.lock /usr/src/app

RUN poetry install --no-root

COPY . .