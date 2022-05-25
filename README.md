# URL Shortner Web App

url-shortner is a project to build a url shortner that can handle large loads while also demostrating a knowlege of full stack development.

## Requirements

Install:

* Python3
* Pip

## Build

### Setup Python virtual environment

1. In repository run,`python3 -m venv flaskEnv`
2. Activate virtual environment, `source ./flaskEnv/bin/activate`
3. Install required package, `pip install -r requirements.txt`

## Running

1. Start MongoDB Server, `docker run -it --rm -p 27017:27017 mongo`
2. Start Flask App, `python run.py`

## Testing

Testing is done using unittest, to start testing, follow the steps

1. Start MongoDB Server, `docker run -it --rm -p 27017:27017 mongo`
2. Start Flask App, `python -m unittest -b`

## Prompt

System design interviews can definitely be tough! Watching system design videos are definitely a good way to get started, but trying to put together and tear apart systems is a great way to get some real world experience that you'll find surprisingly applicable to interview loops.

You can do this at home just by playing around with VMs on your computer. For instance, try and make a link shortener that handles the following actions:

* Given a URL, return a newly created short link to the user (10% of requests)
* Given a short link, redirect them to the matching URL (90% of requests)

Now let's try and scale it up to 10 requests a second. Maybe you'll find that your tiny little app server can't handle it. Let's try and start more processes and add a load balancer in front. Great! It's all snappy again.

Now let's try and scale it up to 100 requests a second. You'll find quickly that perhaps your small database won't handle the load, so you'll need to add caching. Great! We're done!

Now let's try and scale it up to 1000 requests a second. Now the writes are taking too long..hmm. What can we do next? We can try and start a read replica for your database, so reads can go to that second database and writes and go to the primary. This makes sense for our workload since we're 90% reads. Great!

And so on and so forth.

A lot of system design questions seem to be super broad but at least often break down into some of the same components:

* How do you scale this to 10x the traffic?
* Given some new requirement, how do you modify the system?
* What happens when piece X breaks?

Good luck out there!

## Sources

* [Original Prompt from /u/](reddit.com)
* [Flask Rest API -Part:0- Setup & Basic CRUD API](https://dev.to/paurakhsharma/flask-rest-api-part-0-setup-basic-crud-api-4650)
* [URL Shortening 101: How It Works, Use Cases and Examples](https://bitly.com/blog/url-shortening-101-how-it-works-use-cases-and-examples/)
* [https://blog.hubspot.com/marketing/parts-url](https://blog.hubspot.com/marketing/parts-url)