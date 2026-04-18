FROM python:3.12-alpine3.19


RUN echo "https://dl-cdn.alpinelinux.org/alpine/v3.19/main" >> /etc/apk/repositories && \
    echo "https://dl-cdn.alpinelinux.org/alpine/v3.19/community" >> /etc/apk/repositories

RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    tzdata \
    openjdk11-jre \
    curl \
    tar


RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.34-r0/glibc-2.34-r0.apk && \
    apk add --force-overwrite glibc-2.34-r0.apk && \
    rm glibc-2.34-r0.apk


RUN curl -o allure-2.30.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.30.0/allure-commandline-2.30.0.tgz && \
    tar -zxvf allure-2.30.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.30.0/bin/allure /usr/bin/allure && \
    rm allure-2.30.0.tgz


WORKDIR /usr/workspace


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


ENV PATH="/root/.local/bin:${PATH}"


COPY . .


CMD ["python", "-m", "pytest"]