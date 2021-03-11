# Deploy a set of services using swarm
## Create the swarm
First, create a swarm (the address is from the host):
```
$ docker swarm init --advertise-addr=192.168.0.23
```
Then deploy services there. Write down the **worker** token you see:
```
docker swarm join --token SWMTKN-1-1bminvv7a49j11qrk8bos2jpe2jcpi7m8r9waohclb8i3v8t0p-4rc0kep6i2rf8k8086k5nxlkq 192.168.0.23:2377
```
You'll need it later to join a *worker* to the swarm.
Now add a manager token and write it down:
```
$ docker swarm join-token manager 
To add a manager to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-1bminvv7a49j11qrk8bos2jpe2jcpi7m8r9waohclb8i3v8t0p-3hkpbg3xxof0m77j6blosbd76 192.168.0.23:2377

[node1] (local) root@192.168.0.23 ~/docker/swarm-stack
```
Create four more instances (hosts). All together there will be 5 instances:
- 3 managers ad
- 2 workers

Join managers on the second and the third instances. 
Join workers on the fourth and fifth.

Check your work:
```
$ docker node ls
ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
ninowht8woqrudylrbuqvrbad *   node1      Ready     Active         Leader           20.10.0
rt9pgh3b5piees6brrziz81gv     node2      Ready     Active         Reachable        20.10.0
631bh8x439kcgcvychr7pwwns     node3      Ready     Active         Reachable        20.10.0
ax7u4oi9nr0ldx3us2qbkidpy     node4      Ready     Active                          20.10.0
tmalbnhyr6gesx33vgc8p5y7f     node5      Ready     Active                          20.10.0
[node1] (local) root@192.168.0.23 ~/docker/swarm-stack
```
## Setup a simple service
```
docker service create --name web -p 8080:8080 --replicas 3 chernyshevdv/gsd:first-ctr
```
Here is the output:
```
rkog5pytcfhp9qxuhgvm1y73u
overall progress: 3 out of 3 tasks 
1/3: running   [==================================================>] 
2/3: running   [==================================================>] 
3/3: running   [==================================================>] 
verify: Service converged
```
Let's check out:
```
$ docker service ls
ID             NAME      MODE         REPLICAS   IMAGE                        PORTS
rkog5pytcfhp   web       replicated   3/3        chernyshevdv/gsd:first-ctr   *:8080->8080/tcp
```
...and PS:
```
$ docker service ps web
ID             NAME      IMAGE                        NODE      DESIRED STATE   CURRENT STATE           ERROR     PORTS
m2x90b8kwv5y   web.1     chernyshevdv/gsd:first-ctr   node1     Running         Running 2 minutes ago             
6k8jzj5fcba4   web.2     chernyshevdv/gsd:first-ctr   node2     Running         Running 2 minutes ago             
gsb633f54l28   web.3     chernyshevdv/gsd:first-ctr   node3     Running         Running 2 minutes ago
```
Scale up:
```
$ docker service scale web=10
```
## Now setup the stack
### First build the image
Let's recall: it should be `chernhyshevdv/gsd:swarm-stack`
```
$ docker image build -t chernyshevdv/gsd:swarm-stack .
$ docker image push chernyshevdv/gsd:swarm-stack
```
And now deploy the stack!
```
$ docker stack deploy -c docker-compose.yml counter
Creating network counter_counter-net
Creating service counter_web-fe
Creating service counter_redis
```
Check it out:
```
$ docker stack ls
NAME      SERVICES   ORCHESTRATOR
counter   2          Swarm
```
See a list of services:
```
$ docker stack services counter
```
And we can see each container:
```
$ docker stack ps counter
```