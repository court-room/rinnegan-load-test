#!/bin/bash

for filename in server/*.py; do
    locust --host http://backend.rinnegan.io:5000 --locustfile $filename
done
