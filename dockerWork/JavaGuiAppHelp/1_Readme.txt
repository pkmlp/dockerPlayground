
Dieses Beispiel ist eine Erweiterung zum Beispiel JavaGuiApp. 
Es wird ein Browser gestartet, der die Anleitung zur JavaGuiApp CMDB zeigt.


================================
Schritt 1: CMDB-Help-Image bauen
================================

Zuerst erstellen wir ein Dockerfile, mit dem wir ein Image mit dem Firefox Browser erzeugen.

    FROM ubuntu:16.04
    RUN apt-get update && \
            apt-get install -y firefox && \
            apt-get clean
    RUN groupadd --gid 1000 user && \
            useradd --uid 1000 --gid 1000 --create-home user
    USER user


Dann erzeugen wir mit diesem Dockerfile ein Image 
--> Dazu stehen wir wieder im Verzeichnis, in dem auch das Dockerfile liegt

	> docker build -t java_gui_app_help . 



========================================
Schritt 2: Starten des Firefox Container
========================================

    > xhost local:root
	> docker run --detach \
                     --volume /tmp/.X11-unix:/tmp/.X11-unix \
                     --env DISPLAY=unix$DISPLAY \
                     --name Java_GUI_App_Help \
                     java_gui_app_help firefox https://sway.com/3Mp7wKSIHzh8oxJB?ref=Link

