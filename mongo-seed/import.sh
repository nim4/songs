#!/usr/bin/env bash

mongoimport --host ${MONGO_HOST} --collection ${MONGO_COLLECTION} --type json --file ${MONGO_FILE}