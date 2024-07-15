FROM python:3.12

USER root

RUN apt-get update && apt-get install -yy nano curl git

WORKDIR /test

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

ENTRYPOINT [ "/bin/bash" ]

CMD [ "start.sh" ]