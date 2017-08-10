
In diesem Beispiel nehmen wir unsere Datenbank-Entwicklungsumgebung (MySQL & MySQL-Workbench) aus dem Beispiel myThirdApp der MySqlApps, ABER ...

... in diesem Beispiel arbeiten wir mit docker-compose um alles noch einmal stark zu vereinfachen. So werden wir dann z.B. die gesamte Datenbank-Entwicklungsumgebung (MySQL & MySQL-Workbench) mit einem einzigen Befehl starten können.

Damit haben wir dann eine Datenbankumgebung, die komplett Containerisiert ist und dazu noch sehr einfach zu unterhalten ist.




=============================================
Schritt 1: das docker-compose.yaml File bauen
=============================================

Zuerst erstellen wir ein docker-compose.yaml File, das unsere ganze Umgebung beschreibt. Im wesentlichen umfass das yaml-File alle Parameter, die wir bei den einzelnen run commands angegeben haben.




===========================================
Schritt 2: dann starten wir unsere Umgebung
===========================================

    > xhost local:root    
    > docker-compose up -d
    



===========================================
Schritt 3: dann stoppen wir unsere Umgebung
===========================================

    > docker-compose up -d




Wichtige Hinweise:

    > docker-compose logs      --> zeigt die logs der laufenden Services (Container)
    > docker-compose ps        --> zeigt die laufenden Services (Container)

