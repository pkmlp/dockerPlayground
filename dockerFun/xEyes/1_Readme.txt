
==================================
Schritt 1: Docker Image bauen mit:
==================================

    > docker build -t augen .



=======================
Schritt 2: Starten mit:
=======================

    > xhost +local:root
    > docker run -d \
        -e DISPLAY=$DISPLAY \
        -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
        augen xeyes -geometry 150x75+70+35

