FROM python:alpine3.7

LABEL maintainer="Ethan Haynes <ethanhaynes@alumni.harvard.edu>"

RUN mkdir /etc/remote-tools

COPY getDiskUsage.py /etc/remote-tools/getDiskUsage.py

EXPOSE 9999

CMD ["python3", "/etc/remote-tools/getDiskUsage.py"]
