### lab work 1

#### structure:
* facade-service: main access point of system
  * app.py: main API off system
  * Dockerfile: container for facade-service
* logging-service: service that stores messages in memory
  * app.py: logger API
  * Dockerfile: container for logging-service
* messages-service: empty service
  * app.py: empty API
  * Dockerfile: container for messages-service
* docker-compose.yml: start point
* main.py: testing script

**docker-compose.yml usage:**
```shell
$ sudo docker compose up
```

after start `docker compose` run `main.py`:
```shell
$ python3 main.py -m/--method [-t/--text 'text message']
```

**main.py usage:**
```text
$ python3 main.py -h

    script to test microservice lab
    
    -h           print this help message and exit           | OPTIONAL
    -m/--method  [GET, POST] method for testing             | REQUIRED
    -t/--text    text of message to insert for POST method  | REQUIRED/OPTIONAL
```
