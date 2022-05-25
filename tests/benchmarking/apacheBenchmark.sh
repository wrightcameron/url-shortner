#!/bin/bash
# Don't point this at a third party server, it's equal to a DOS.
# Also the server needs to be online for this to work, and mongo db needs to have data
server=$1

# First Test
echo "Basic Benchmark, 100 get requests with 10 sent at a time"
ab -n 100 -c 10 $server/api/link


