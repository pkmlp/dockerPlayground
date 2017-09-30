
=============================================
Erstellen eines Images mit Latex und TexLive
=============================================

Das dafür benötigte Dockerfile ist (muss) im aktuellen Verzeichnis (sein).
Das Image erhält den Namen texmaker.

    > docker build -t texmaker .


======================================
Starten des Images mit Namen texmaker
======================================

    > xhost local:root
    > docker run -it --rm=true \
        -e USER=$USER -e USERID=$UID \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -e DISPLAY=unix$DISPLAY \
        --device /dev/dri \
        -v $HOME:/home/texmaker \
        --name texmaker \
        texmaker
