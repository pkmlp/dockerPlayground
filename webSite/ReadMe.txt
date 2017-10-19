
Einen Container mit einer eigenen WebSite erstellen:

Ausgangslage / Lösungsbeschreibung: 
- Die WebSite steht im aktuellen Arbeitsverzeichnis im Unterverzeichnis htdocs
- Dieses Unterverzeichnis wird dem Container als /usr/local/apache2/htdocs gemounted
- Port 80 im Container (Standard-Port des Apache WebServers) wird auf Port 80 im Host gemounted



================================================================================================
Schritt 1: Erstellen eines Containers mit Namen myApacheServer basierend auf dem Image httpd:2.4 
================================================================================================

    > docker run \
             --detach \
             --name myApacheServer \
             -p 80:80 \
             -v $(pwd)/htdocs:/usr/local/apache2/htdocs \
             httpd:2.4



===========================================
Schritt 2: Die WebSite im Browser aufrufen:
===========================================

    > firefox localhost:80/helloWorld.html
