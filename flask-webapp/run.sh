#!/bin/bash

# TODO If we don't have reverse proxy need to change the bind address
gunicorn --bind 127.0.0.1:8000 --daemon --workers 1 --timeout 600 app:app
# Check if gunicron could start properly
status=$?
if [ status -ne 0 ]; then
    echo "failed to start Flask webapp"
    exit $status
fi;
# TODO Make sure that date time is formated correctly.
echo "Started Flask Server at ${date}"

#TODO Eventually we will want the logs from this server to go somewhere more perminate.