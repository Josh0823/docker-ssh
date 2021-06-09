FROM ubuntu:latest

RUN \
    apt-get update          &&  \
    apt-get upgrade --yes   &&  \
    apt-get install --yes       \
        openssh-server

# Configure sshd

RUN \
    mkdir -p /var/run/sshd

ADD ./srv/bin/conda /tmp/bin/conda
RUN echo "export PATH=/tmp/bin:${PATH}" > /etc/environment

RUN \
    adduser -q --gecos "" --disabled-password admin     && \
    echo admin:admin | chpasswd

RUN \
    adduser -q --gecos "" --disabled-password user1     && \
    echo user1:user1 | chpasswd

WORKDIR /srv
ADD docker-entrypoint.sh /tmp
RUN chmod +x /tmp/docker-entrypoint.sh
ENTRYPOINT [ "bash", "/tmp/docker-entrypoint.sh" ]
CMD [ "/usr/sbin/sshd", "-p", "22", "-D" ]
