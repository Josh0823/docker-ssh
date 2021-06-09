FROM ubuntu:latest

WORKDIR /srv

RUN \
    apt-get update          &&  \
    apt-get upgrade --yes   &&  \
    apt-get install --yes       \
    openssh-client          \
    python3                 \
    python3-pip

RUN pip install asyncssh

RUN \
    adduser -q --gecos "" --disabled-password admin     && \
    echo admin:admin | chpasswd

RUN \
    adduser -q --gecos "" --disabled-password user1     && \
    echo user1:user1 | chpasswd

WORKDIR /root
ADD docker-entrypoint.sh /srv
RUN chmod +x /srv/docker-entrypoint.sh
ENTRYPOINT [ "/srv/docker-entrypoint.sh" ]
CMD ["sleep", "9999"]
