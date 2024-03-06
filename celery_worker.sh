#!/bin/sh

until cd /file
do
    echo "Waiting for server volume..."
done

celery -A file worker -l -info
