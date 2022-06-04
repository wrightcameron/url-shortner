#!/bin/bash
# Don't point this at a third party server, it's equal to a DOS.
# Also the server needs to be online for this to work, and mongo db needs to have data

runBenchmark () {
    server=$1
    requests=$2
    concurrency=$3
    echo "Benchmarking Shell Script for testing url shortner"

    # Post System hardware, though this will only matter if the this script is run on server.
    echo "Getting hardware info"
    echo "- CPU"
    lscpu | head
    echo "- Memory"
    free -h

    # First Test, list all links on an empty database.
    echo -e "\n[TEST 1]: Basic Benchmark, $requests get requests with $concurrency sent at a time of all urls"
    ab -n $requests -c $concurrency $server/api/link

    # Second Test, test write.  Add the same link over and over again, currently the database doesn't care about duplicate links
    echo -e "\n[TEST 2]: Test write.  Add the same link over and over again, currently the database doesn't care about duplicate links"
    echo '{"url":"https://google.com"}' > /tmp/post.data
    ab -T 'application/json' -n $requests -c $concurrency -p /tmp/post.data $server/api/link


    echo -e "\n[TEST 3]: Basic Benchmark, $requests get requests with $concurrency sent at a time, same all urls check for increased time"
    ab -n $requests -c $concurrency $server/api/link

    echo -e "\n[TEST 4]: $requests get requests with $concurrency sent at a time, same url with same link"
    # curl "localhost:5000/api/link" | python -c "import sys, json; data=json.load(sys.stdin); print([d['_id'] for d in data])"
    # TODO Add a paramater to the api/link get route to either limit responses back or get a random url with tags.  Incase of caching
    urlId=$(curl "${server}/api/link" | python -c "import sys, json; data=json.load(sys.stdin); print(data[0]['_id']['\$oid'])")
    ab -n $requests -c $concurrency $server/api/link/$urlId

    echo -e "\n[TEST 5]: Concurrency test with writes and reads at same time."
    #TODO Need to split the requests into 90% reads and 10% writes, figure out how to do this with bash.
    ab -n $requests -c $concurrency $server/api/link/$urlId > /tmp/test1.txt &
    ab -T 'application/json' -n $requests -c $concurrency -p /tmp/post.data $server/api/link > /tmp/test2.txt &
    wait
    echo -e "\n[PART 1]: Read Results"
    cat /tmp/test1.txt && rm -f /tmp/test1.txt
    echo -e "\n[PART 2]: Write Results"
    cat /tmp/test2.txt && rm -f /tmp/test2.txt

    # Clean up
    rm -f /tmp/post.data
};

server=$1
requests=$2
concurrency=$3

if [ -z $server ]; then
    server="localhost:5000"
fi;
if [ -z $requests ]; then
    requests=100
fi;
if [ -z $concurrency ]; then
    concurrency=10
fi;

runBenchmark $server $requests $concurrency;
#TODO Add more test data to mongoDB, see how an increasing database effects performance.
