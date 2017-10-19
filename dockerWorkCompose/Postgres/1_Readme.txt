
PostgreSQL Umgebung mit PostgreSQL-Server und dem Web-GUI Adminer 



=============================================
Schritt 1: das docker-compose.yaml File bauen
=============================================

Zuerst erstellen wir ein docker-compose.yaml File, das unsere ganze Umgebung beschreibt. 



===========================================
Schritt 2: dann starten wir unsere Umgebung
===========================================

    > docker-compose up -d
    


===========================================================
Schritt 3: dann arbeiten wir mit unserer Umgebung (Adminer)
===========================================================

    > firefox localhost:8080



===========================================
Schritt 4: dann stoppen wir unsere Umgebung
===========================================

    > docker-compose stop



Wichtige Hinweise:

    > docker-compose logs      --> zeigt die logs der laufenden Services (Container)
    > docker-compose ps        --> zeigt die laufenden Services (Container)

