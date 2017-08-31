
==========================================================================
Schritt 1: Python-Image bauen, in das gleich die Python-App übergeben wird
==========================================================================

Zuerst erstellen wir ein Dockerfile, mit dem wir ein Image mit Python und PyQT erzeugen und
in das wir die Python-App mit allen dazugehörigen Dateien hineinkopieren.

    > FROM ubuntu:16.04
    > RUN apt-get update
    > RUN apt-get install -y python3 python3-pyqt5
    > COPY . /usr/src/PythonGuiApp
    > WORKDIR /usr/src/PythonGuiApp


Dann erzeugen wir mit diesem Dockerfile ein Image 
--> Dazu stehen wir wieder im Verzeichnis, in dem auch das Dockerfile liegt

	> docker build -t python_gui_app . 



=======================================
Schritt 2: Starten den Python Container
=======================================

    > xhost local:root
	> docker run --detach \
                 --volume /tmp/.X11-unix:/tmp/.X11-unix \
                 --env DISPLAY=unix$DISPLAY \
                 --name Python_GUI_App \
                 python_gui_app python3 /usr/src/PythonGuiApp/pkmlpCounter.py

