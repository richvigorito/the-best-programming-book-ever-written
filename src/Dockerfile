FROM debian:bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    vim-tiny \
    fpc \
    python3 \
    g++ \
    golang-go \
    make \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

CMD ["make", "help"]
