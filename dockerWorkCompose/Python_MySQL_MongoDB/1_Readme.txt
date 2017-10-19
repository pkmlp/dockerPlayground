
In diesem Beispiel erstellen wir eine Datenbank-Entwicklungsumgebung (MySQL mit MySQL-Workbench, MongoDB mit , PythonJupyter).



=============================================
Schritt 1: das docker-compose.yaml File bauen
=============================================

Zuerst erstellen wir ein docker-compose.yaml File, das unsere ganze Umgebung beschreibt. 



===========================================
Schritt 2: dann starten wir unsere Umgebung
===========================================

    > xhost local:root    
    > docker-compose up -d
    


===========================================
Schritt 3: dann stoppen wir unsere Umgebung
===========================================

    > docker-compose stop



Wichtige Hinweise:

    > docker-compose logs      --> zeigt die logs der laufenden Services (Container)
    > docker-compose ps        --> zeigt die laufenden Services (Container)


    Es kann vorkommen, dass mit dem Mongo-Gui keine Verbindung erstellt werden kann. 
    Dann den Container mit dem Mongo_Gui einfach noch mal starten (restart). 
    Dies passiert, wenn das Mongo_Gui versucht sich zum Mongo_Server zu verbinden, 
    bevor dieser up and running ist.

    Dem MySQL Server ist ein Volume für SQL-Scripts gemounted. Um diese ausführen zu können, 
        > docker exec -it MySQL_Server bash   --> öffnene einer Bash-Shell im Container
        > mysql -u root -p < scriptname.sql   --> führt das Script aus

    PythonJupyter: Der Mongo Server kann nicht über den hostname angesprochen werden.  
    Mit der IP Adresse funktioniert es aber (keine Ahnung wieso). 
    Die IP Adresse ist zu finden mit:
        > docker inspect Mongo_Server         --> unter config ist die IP Adresse zu finden
