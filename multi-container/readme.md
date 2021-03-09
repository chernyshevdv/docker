# A python app with a kind of microservices
This solution contains a web server and redis cache service.
The following activities need to be performed to build and run the solution.
```
$ docker login
$ git clone https://github.com/chernyshevdv/docker
$ cd docker/multi-container
$ docker-compose up -d
```
And that's it!
Remove "-d" if you don't want it detached.