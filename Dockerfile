FROM registry.cirrus.ibm.com/public/ubi8:latest

LABEL maintainer="Ivan.Warlock@outlook.com"

ARG ARGO_USER_HOME=/app
ENV ARGO_HOME=${ARGO_USER_HOME}

RUN dnf update -y && dnf install \
make \
systemd-libs \
systemd-udev \
systemd-pam \
gcc \
gcc-c++ \
openssl-devel \
bzip2-devel \
nano \
nc \
wget \
python39 -y

#from local Repository
COPY . /app

#list the files inside app folder
RUN ls -1a /app
RUN useradd -ms /bin/bash -d ${ARGO_HOME} argo
RUN echo "argo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN chown -R argo: ${ARGO_HOME}
RUN chown argo ${ARGO_HOME}
RUN chmod +x ${ARGO_HOME}
RUN chmod 777 ${ARGO_HOME}

USER argo
#define work space
WORKDIR /app

# confirm installation

RUN python3 --version
RUN pip3 install -r /app/requirements39.txt

#expose app port
EXPOSE 3000