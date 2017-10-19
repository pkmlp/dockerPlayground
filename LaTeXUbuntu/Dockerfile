
FROM ubuntu:17.04 

ENV DEBIAN_FRONTEND noninteractive

RUN rm /bin/sh && ln -s /bin/bash /bin/sh 
ENV LC_ALL C.UTF-8 
ENV LANG C.UTF-8 
RUN sed -i 's/ universe/ universe multiverse/' /etc/apt/sources.list 
RUN apt update && \
    apt upgrade -y && \
    apt dist-upgrade -y && \
    apt install -y \
    git \
    wget \
    xvfb \
    flex \
    dh-make \
    debhelper \
    checkinstall \
    fuse \
    snapcraft \
    bison \
    libxcursor-dev \
    libxcomposite-dev \
    software-properties-common \
    build-essential \
    libssl-dev \
    libxcb1-dev \
    libx11-dev \
    libgl1-mesa-dev \
    libudev-dev \
    qt5-default \
    libqt5script5 \
    qtbase5-private-dev &&\
    apt clean

RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list 
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    texlive-generic-recommended \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-extra-utils \
    texlive-font-utils \
    texlive-xetex \
    texlive-luatex \
    texlive-lang-german \
    fonts-lmodern \
    fonts-font-awesome \
    && apt-get autoclean -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* 

RUN wget http://www.xm1math.net/texmaker/assets/files/texmaker_5.0.2_ubuntu_17_04_amd64.deb 
RUN apt-get install -f ./texmaker_5.0.2_ubuntu_17_04_amd64.deb -y

RUN useradd texmaker \
    && mkdir /home/texmaker \
    && chown texmaker:texmaker /home/texmaker 
    
USER texmaker 
WORKDIR /home/texmaker 

ENTRYPOINT [ "texmaker" ]
