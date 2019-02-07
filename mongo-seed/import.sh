#!/usr/bin/env bash
set -e

mongoimport --host ${MONGO_HOST} --db ${MONGO_DATABASE} --collection ${MONGO_COLLECTION} --type json --file ${MONGO_FILE}