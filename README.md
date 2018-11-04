# HOW TO RUN
```sh
    $ docker build . -t remote-tools/getdisk 
    $ docker run --rm -d -p 9999:9999 --read-only=true --tmpfs /run --tmpfs /tmp -v "$(pwd)":/app:ro remote-tools/getdisk:latest
```
