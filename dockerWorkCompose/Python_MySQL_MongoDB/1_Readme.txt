
In diesem Beispiel erstellen wir eine Datenbank-Entwicklungsumgebung: 
 - MySQL-Server mit MySQL-PhpMyAdmin, 
 - MongoDB mit MongoExpress, 
 - PythonJupyter


=============================================
Schritt 1: das docker-compose.yaml File bauen
=============================================

Zuerst erstellen wir ein docker-compose.yaml File, das unsere ganze Umgebung beschreibt. 
Vor dem Starten der Umgebung sicherstellen, dass nicht bereits ein DB-Server läuft 
 --->  anders formuliert: sicherstellen, dass die von den Containern benötigten Ports 
       nicht schon belegt/benutzt sind.

    > sudo service mongodb stop 
    > sudo service mysql stop


===========================================
Schritt 2: dann starten wir unsere Umgebung
===========================================

    > docker-compose up -d


=================================================
Schritt 3: dann arbeiten wir mit unserer Umgebung
=================================================

  Alle UIs sind Browser-UIs (siehe auch docker-compose.yaml File)

    > Python-GUI:   http://192.168.0.10:8888   für PythonJupyter
    > MongoDB-GUI:  http://192.168.0.20:8081   für MongoExpress
    > MySQL-GUI:    http://192.168.0.50:80     für PhpMyAdmin

    Dem MySQL Server ist ein Volume mit einem SQL-Script gemounted (siehe: docker-compose.yaml). 
    Um dieses SQL-Script (erstellt die MySQL Datenbank Heizungsmonteur) ausführen zu können:
        > docker exec -it MySQL_Server bash

    Dann in das entsprechende Verzeichnis wechseln:
        > cd /usr/src/mysqlScripts

    Dann das Script ausführen:
        > mysql -u root -p < Heizungsmonteur_Erstellen_InnoDB.sql



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

    PythonJupyter: Der Mongo Server kann nicht über den hostname angesprochen werden.  
    Mit der IP Adresse funktioniert es aber (keine Ahnung wieso). 
    Die IP Adresse ist zu finden mit:
        > docker inspect Mongo_Server         --> unter config ist die IP Adresse zu finden
