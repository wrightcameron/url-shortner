# URL Shortner Project

url-shortner is a project to build a url shortner that can handle large loads while also demostrating a knowlege of full stack development.

## Requirements

Install:

* docker & docker-compose

## Build

1. Change directory to root dir of repository
2. Run command, `docker-compose build`

## Running

### Production

1. Run command, `docker-compose up -d`

### Development

Running this project for development or testing, its better to run each component indivudually or not in docker.
As the Flask backend contains the most setup and testing view the readme in directory *flask-webapp*.

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

[Original Prompt from /u/gooeyblob/](https://www.reddit.com/r/cscareerquestions/comments/8na87e/were_reddit_engineers_here_to_answer_your/dzu3jgu/?context=3)

## Sources

* [Flask Rest API -Part:0- Setup & Basic CRUD API](https://dev.to/paurakhsharma/flask-rest-api-part-0-setup-basic-crud-api-4650)
* [URL Shortening 101: How It Works, Use Cases and Examples](https://bitly.com/blog/url-shortening-101-how-it-works-use-cases-and-examples/)
* [The 5 Basic Parts of a URL: A Short Guide](https://blog.hubspot.com/marketing/parts-url)
* [Run a Django App with Gunicron in Ubuntu](https://rahmonov.me/posts/run-a-django-app-with-gunicorn-in-ubuntu-16-04/)
* [Deploy and Secure a React — Flask App With Docker and Nginx](https://medium.com/swlh/deploy-and-secure-a-react-flask-app-with-docker-and-nginx-768ca582863b)
* [How To Set Up Flask with MongoDB and Docker](https://www.digitalocean.com/community/tutorials/how-to-set-up-flask-with-mongodb-and-docker)