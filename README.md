# HOW TO RUN
```sh
  $ docker build . -t remote-tools/getdisk 
  $ docker run --rm -d -p 9999:9999 --read-only=true --tmpfs /run --tmpfs /tmp -v "$(pwd)":/app:ro remote-tools/getdisk:latest
```

# HOW TO TEST

### Request
```sh
  $ curl http://localhost:9999/app
```
### Response
```sh
  {
    "files": {
      "/app/Dockerfile": 4,
      "/app/getDiskUsage.py": 4,
      "/app/README.md": 4,
      ...
    }
  }
```

## Requirements
### Supported architectures:
amd64, arm32v5, arm32v6, arm32v7, arm64v8, i386, ppc64le, s390x, windows-amd64

### Supported Docker versions:
the latest release (down to 1.6 on a best-effort basis)
