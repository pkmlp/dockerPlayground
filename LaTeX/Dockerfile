FROM debian:stretch 
MAINTAINER Julien Giovaresco <dev@giovaresco.fr> 

RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list 

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    texmaker \
    texlive-generic-recommended \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-extra-utils \
    texlive-font-utils \
    texlive-xetex \
    texlive-luatex \
    fonts-lmodern \
    fonts-font-awesome \
    && apt-get autoclean -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* 
    
RUN useradd texmaker \
    && mkdir /home/texmaker \
    && chown texmaker:texmaker /home/texmaker 
    
USER texmaker 
WORKDIR /home/texmaker 

ENTRYPOINT [ "texmaker" ]
