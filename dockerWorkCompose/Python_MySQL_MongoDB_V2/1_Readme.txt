
In diesem Beispiel erstellen wir eine Datenbank-Entwicklungsumgebung (MySQL mit MySQL-Workbench, MongoDB mit MongoExpress, PythonJupyter).


=============================================
Schritt 1: das docker-compose.yaml File bauen
=============================================

Zuerst erstellen wir ein docker-compose.yaml File, das unsere ganze Umgebung beschreibt. 
Vor dem Starten der Umgebung sicherstellen, dass nicht bereits DB-Server laufen 
 --->  anders formuliert: sicherstellen, dass die von den Copntainern benötigten Ports 
       nicht schon belegt/benutzt sind.

    > sudo service mongodb stop 
    > sudo service mysql stop



===========================================
Schritt 2: dann starten wir unsere Umgebung
===========================================

    > xhost local:root   (ist nur nötig, wenn einer der Container ein X11 GUI (z.B.MySQL Workbench) hat) 
    > docker-compose up -d
    


=================================================
Schritt 3: dann arbeiten wir mit unserer Umgebung
=================================================

  Die UIs für Jupyter und MongoDB sind Browser-UIs (siehe auch docker-compose.yaml File)

    > Python-GUI:   http://192.168.0.10:8888   für PythonJupyter
    > MongoDB-GUI:  http://192.168.0.20:8081   für MongoExpress

  Das UI für MySQL (MySQL_Gui) ist ein X11-Container und startet automatisch.

    Für die Connection der MySQL-Workbench zum Server gelten:
    - hostname: MySQL_Server
    - password: pkmlp



===========================================
Schritt 4: dann stoppen wir unsere Umgebung
===========================================

    > docker-compose stop



Wichtige Hinweise:

    > docker-compose logs      --> zeigt die logs der laufenden Services (Container)
    > docker-compose ps        --> zeigt die laufenden Services (Container)


    Es kann vorkommen, dass mit dem Mongo-Gui keine Verbindung erstellt werden kann. 
    Dann den Container mit dem Mongo_Gui einfach noch mal starten (restart). 
    Dies passiert, wenn das Mongo_Gui versucht sich zum Mongo_Server zu verbinden, 
    bevor dieser up and running ist.

    Dem MySQL Gui (MySQL-Workbench) ist ein Volume für SQL-Scripts gemounted (/usr/src/mysql).
    Das darin enthaltene Script kann aus der Workbench mit Open SQL-Script geöfnet werden.
    
    PythonJupyter: Der Mongo Server kann nicht über den hostname angesprochen werden.  
    Mit der IP Adresse funktioniert es aber (keine Ahnung wieso). 
    Die IP Adresse ist zu finden mit:
        > docker inspect Mongo_Server         --> unter config ist die IP Adresse zu finden
