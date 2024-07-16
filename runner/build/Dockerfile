FROM python:3.12

USER root

RUN apt-get update && apt-get install -yy nano curl git && \
pip install Appium-Python-Client pytest-playwright && playwright install --with-deps

WORKDIR /test

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

ENTRYPOINT [ "/bin/bash" ]

CMD [ "start.sh" ]