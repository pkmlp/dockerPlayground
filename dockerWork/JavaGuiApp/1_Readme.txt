
======================================================================
Schritt 1: Java-Image bauen, in das gleich die Java-App übergeben wird
======================================================================

Zuerst erstellen wir ein Dockerfile, mit dem wir ein Image mit dem JRE erzeugen können und
in das wir die bereits kompilierte Java-App mit allen dazugehörigen Dateien hineinkopieren.

    FROM openjdk
    COPY . /usr/src/JavaGuiApp
    WORKDIR /usr/src/JavaGuiApp


Dann erzeugen wir mit diesem Dockerfile ein Image 
--> Dazu stehen wir wieder im Verzeichnis, in dem auch das Dockerfile liegt

	> docker build -t java_gui_app . 



=====================================
Schritt 2: Starten des Java Container
=====================================

    > xhost local:root
	> docker run --detach \
                     --volume /tmp/.X11-unix:/tmp/.X11-unix \
                     --env DISPLAY=unix$DISPLAY \
                     --name Java_GUI_App \
                     java_gui_app java -jar /usr/src/JavaGuiApp/CaseManagementSQLite.jar

