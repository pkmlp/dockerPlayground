Docker Portainer ist ein GUI zu Docker, das als Container läuft. Prinzipiell lassen sich alle Aufgaben, die im Zusammenhang mit Docker anfallen, 
über dessen Kommandozeilenwerkzeug erledigen. Für einen schnellen Überblick wäre eine grafische Benutzeroberfläche allerdings gelegentlich praktisch. 
Portainer schafft Abhilfe.

Folgende Befehle erstellen den Portainer Container:

    > docker volume create portainer_data
    > docker run -d -p 9000:9000 \
                 -v /var/run/docker.sock:/var/run/docker.sock \
                 -v portainer_data:/data \
                 portainer/portainer

Das GUI (Portainer) kann dann mit einem Internet-Browser mit localhost:9000 gestartet werden.

Portainer ist eine grafische Oberfläche für Docker, mit der man sich einen raschen Überblick über den Zustand eines Hosts beziehungsweise eines 
Clusters verschaffen kann.

Mehr dazu bei heise.de : https://www.heise.de/developer/artikel/Eine-UI-fuer-Docker-3492372.html 
