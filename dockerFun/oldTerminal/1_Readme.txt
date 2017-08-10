
Hier ein Beispiel, in dem eine GUI-App im Container gestartet wird und die GUI-Ausgabe wird auf den X11 Server im HOST umgeleitet. Die GUI-App simuliert das Erscheinungsbild eines ur-alten Terminals. Ist nicht wirklich zu gebrauchen, zeigt aber, was mit Docker möglich ist.




Mit dem Dockerfile in diesem Verzeichnis kann das Docker-Image erstellt werden:

    > docker build -t oldterminal .



Wichtige Hinweise: 

1) Der Punkt am Ende der Zeile ist wichtig, da mit diesem der Ort des Dockerfile mitgegeben wird. Da sich das Dockerfile in diesem Verzeichnis befindet, reicht der Punkt (als aktuelles Verzeicnis) aus.

2) Das Erstellen dieses Images kann durchaus etwas dauern. Es sollte jedoch funktionieren, auch wenn es scheint, als ob viele Fehlermeldungen während der Erstellung erscheinen.






Das Image kann dann ausgeführt werden mit:

    > xhost local:root
    > docker run --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY --name oldTerminal  oldterminal






