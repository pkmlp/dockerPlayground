FROM ubuntu:16.04
RUN apt-get update && \
        apt-get install -y firefox && \
        apt-get clean
RUN groupadd --gid 1000 pkmlp && \
        useradd --uid 1000 --gid 1000 --create-home pkmlp
USER pkmlp
CMD firefox https://sway.com/3Mp7wKSIHzh8oxJB?ref=Link
