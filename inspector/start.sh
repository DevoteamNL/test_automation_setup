#!/bin/bash

docker run --rm --name inspector \
    --privileged \
    -v /dev/shm:/dev/shm \
    -v /tmp/.X11-unix/:/tmp/.X11-unix/ \
    -e DISPLAY=unix$DISPLAY \
    mcr.microsoft.com/playwright:v1.44.1 npx -y playwright open google.com
