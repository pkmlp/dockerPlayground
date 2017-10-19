
==================================================
Schritt 1: Erstellen des Images mit dem Dockerfile
==================================================

docker build -t mongoserver .



==================================
Schritt 2 Erstellen des Containers
==================================

docker run -d \
--name MongoDB_Server \
-e MONGODB_ADMIN_USER=mongoAdmin \
-e MONGODB_ADMIN_PASS=pkmlp \
-p 27017:27017 \
mongoserver 



============================
Schritt 3: Testn des Servers
============================

docker exec -it MongoDB_Server bash 
mongo -u mongoAdmin -p --authenticationDatabase "admin"
