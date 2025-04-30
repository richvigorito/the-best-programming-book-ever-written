FROM debian:bullseye

RUN apt-get update && \
    apt-get install -y \
    vi \
    fpc \
    python3 \
    g++ \
    golang-go \
    make \
    && apt-get clean

WORKDIR /app
COPY . /app

CMD ["make", "help"]

