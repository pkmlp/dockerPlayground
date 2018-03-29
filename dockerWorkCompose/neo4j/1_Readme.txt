#
# Neo4j Graph Database 
#


=============================================
Schritt 1: das docker-compose.yaml File bauen
=============================================

Zuerst erstellen wir ein docker-compose.yml File, das unsere ganze Umgebung beschreibt. 

Version 1 --> ohne Authentisierung

version: '2'
services:
  neo4j: 
      image: neo4j:latest
      container_name: neo4j
      volumes:
          - /home/pkmlp/neo4j/data:/data/dbms
      ports: 
          - "7474:7474" 
          - "7687:7687" 
      environment: 
          NEO4J_AUTH: "none"


Version 2 --> mit Authentisierung (neo4j/neo4j)

version: '2'
services:
  neo4j: 
      image: neo4j:latest
      container_name: neo4j
      volumes:
          - /home/pkmlp/neo4j/data:/data/dbms
      ports: 
          - "7474:7474" 
          - "7687:7687" 



===========================================
Schritt 2: dann starten wir unsere Umgebung
===========================================

    > docker-compose up -d
    


===========================================================
Schritt 3: dann arbeiten wir mit unserer Umgebung (Adminer)
===========================================================

    > firefox localhost:7474



===========================================
Schritt 4: dann stoppen wir unsere Umgebung
===========================================

    > docker-compose stop



============================================================================
Schritt 5: und räumen (bei Bedarf) die DB, Images, Container, etc wieder weg
============================================================================

    > sudo rm -r /home/pkmlp/neo4j/data
    > /home/pkmlp/myTools/dockerCleanup



Wichtige Hinweise:

    > docker-compose logs      --> zeigt die logs der laufenden Services (Container)
    > docker-compose ps        --> zeigt die laufenden Services (Container)

