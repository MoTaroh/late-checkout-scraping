FROM python:3.8.9
RUN set -x && \
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH /root/.poetry/bin:$PATH
RUN poetry config virtualenvs.create false