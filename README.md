# HOW TO RUN
```sh
    $ docker run -it --read-only=true --tmpfs /run --tmpfs /tmp -v "$(pwd)":/app:ro python:alpine3.7 ash
```
