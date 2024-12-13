FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -qy gcc gcc-multilib xinetd

RUN useradd -m chal
RUN chown -R root:root /home/chal
RUN chmod -R 755 /home/chal

CMD ["/usr/sbin/xinetd", "-dontfork"]
