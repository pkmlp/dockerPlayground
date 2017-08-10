
In diesem Beispiel arbeiten wir wieder (siehe unbedingt auch myFirstDbApp und mySecondDbApp) mit MySQL, ABER ... 

... in diesem Beispiel wollen wir den Container-Gedanken (alles in Container verpacken und pro Container ein Service) komplett berücksichtigen und darum bauen wir ein Szenario mit zwei Containern und einem named Volume für die Daten der Datenbank (die wollen wir ja persitent halten). Die beiden Container sind über ein Docker-Netzwerk miteiunander verbunden.

 - der erste Container enthält den DB-Server 
 - der zweite Container enthält  die MySQL Workbench, mit der wir auf dem Db-Server arbeiten wollen
 - das nemad Volume enthält die Daten des DB-Severs, die persitent gehalten werden sollen.
 - das Docker Netzwerk erlaubt die Kommunikation unter den beiden Containern

Damit haben wir dann eine Datenbankumgebung, die komplett Containerisiert ist.




========================================
Schritt 1: Image für der DB-Server bauen
========================================

Zuerst erstellen wir ein Dockerfile, mit dem wir das Image für den DB-Server erzeugen können. Dazu verwenden wir als Basis das MySQL-Image von Docker und setzen lediglich noch das root Passwort für den DB-Server.

	FROM mysql:5.7 
	MAINTAINER Peter Kessler <pkmlp@pkmlp.ch> 
	ENV MYSQL_ROOT_PASSWORD=pkmlp


Dann erzeugen wir mit diesem Dockerfile ein Image (wir stehen wieder im Verzeichnis, in dem das Dockerfile ist)

        > docker build -t db_server .




=================================
Schritt 2: Image für DB-GUI bauen
=================================

Zuerst erstellen wir ein Dockerfile, mit dem wir ein Image erzeugen können, dass lediglich die MySQL Workbench enthält

	FROM ubuntu:latest 
	MAINTAINER Peter Kessler <pkmlp@pkmlp.ch> 
	ENV DEBIAN_FRONTEND noninteractive 
	RUN apt-get update && apt-get install -y mysql-workbench 
	CMD mysql-workbench


Dann erzeugen wir mit diesem Dockerfile ein Image (wir stehen wieder im Verzeichnis, in dem das Dockerfile ist)

	> docker build -t db_gui . 






===============================================================================================
Schritt 3: Das Data-Volume und das Docker-Netz erstellen und darin die beiden Container starten
===============================================================================================

Zuerst erstellen wir ein Docker-Netz für unsere beiden Container

    > docker network create --driver bridge db_netz


Dann erstellen wir das Data-Volume für die persistenten Daten

    > docker volume create db_daten


Dann starten wir den DB-Server Container im erstellen Netz und verlinken das Volumne db_daten mit dem Data-Directorie im Container

    > docker run --detach \
                 --network=db_netz \
                 --name DB_Server  \
                 --volume db_daten:/var/lib/mysql   \
                 db_server


Dann starten wir den DB-GUI Container

    > xhost local:root
	> docker run --detach \
                     --network=db_netz \
                     --volume /home/pkmlp/gitRepos/dockerPlayground/dockerWork/MySqlApps/myThirdApp/DB_Gui/mySqlShare:/usr/src/mysql   \
                     --volume /tmp/.X11-unix:/tmp/.X11-unix \
                     --env DISPLAY=unix$DISPLAY \
                     --name DB_Gui \
                     db_gui 



Wichtige Hinweise:

Somit haben wir eine Datenbankumgebung aufgebaut, die komplett Containerisiert ist. Alle Applikationen sind in Containern. Die Daten sind Persistent auf dem Docker Host gespeichert. 


Wenn man sehen möchte wo die denn im DOcker Host abgelegt sind:

    > docker volume inspect db_daten


 







