
Einen Container mit einem Ubuntu in dem VIM läuft erstellen

====================================
Schritt 1: Erstellen des Dockerfile
====================================

    FROM ubuntu:16.04
    MAINTAINER Peter Kessler

    RUN apt-get update &&       \
        apt-get install -y vim 

Hinweis:
- das File sollte Dockerfile heissen (muss nicht, macht es aber an dieser Stelle einfacher)



====================================================
Schritt 2: Erstellen eines Images mit dem Dockerfile
====================================================

    > docker build -t myubuntu .

Hinweise:
- das Flag -t (Tag) bedeutet, dass ich dem Image den Namen myUbuntu gebe.
- der Punkt (.) bedeutet, dass das Dockerfile für das bauen des Images im aktuellen Verzeichnis steht.
- Der Name des Images muss in Kleinbuchstaben sein.



=================================================================
Schritt 3: Starten des Containers mit dem soeben erstellten Image
=================================================================

    > docker run \
            -it \
            --name myUbuntu \
            myubuntu bash

Hinweise:
- das Flag -it bedeutet, das der Container im Interaktiven Modus (i) mit einem Terminal (t füt tty) gestartet wird
- das Flag --name definiert den Namen den der Container erhalten soll (darf Grossbuchstaben enthalten)
- myubuntu definiert den Namen des zu verwendenden Images
- bash ist die Shell die gestartet werden soll  



=========================================================
Schritt 4: vim im Container (in der bash Session) starten
=========================================================

    > vim

Hinweise:
- die bash wird als root gestartet 
