# nodejs web app
To build an image and run it in a conainer, execute the following commands:
```
$ git clone https://github.com/chernyshevdv/docker
$ cd docker/single-container
$ docker image build .
$ docker image push chernyshevdv/gsd:first-ctr
$ docker container run -d --name web -p 8000:8080
```