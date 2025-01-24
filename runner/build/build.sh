#!/bin/bash

echo starting build....

docker build . -t runner:playwright

echo build finished