
In diesem Beispiel nehmen wir die JavaGuiApp (CMDB) als Grundlage ABER ...

... in diesem Beispiel arbeiten wir mit docker-compose um alles noch einmal stark zu vereinfachen, so dass wir den Container mit der App und den Container mit der Help mit einem einzigen Befehl starten können.



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

    > docker-compose stop 




Wichtige Hinweise:

    > docker-compose logs      --> zeigt die logs der laufenden Services (Container)
    > docker-compose ps        --> zeigt die laufenden Services (Container)

