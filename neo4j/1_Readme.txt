#
# neo4j Graph Database
#

Dieses Verzeichnis enthält ein Beispiel für eine neo4j Graph Database

Um den neo4j Container (ohne Authentifizierung) zu starten:

docker run \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --env=NEO4J_AUTH=none \
    --name=neo4j  \
    neo4j

Um den neo4j Container (mit Authentifizierung) zu starten:

docker run \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --name=neo4j  \
    neo4j

    By default Neo4j requires authentication. 
    You have to login with neo4j/neo4j at the 
    first connection and set a new password.


Zugriff auf das GUI des neo4j Containers im Webbrowser mit
    http://localhost:7474


Hinweise:

   Die DB wird im Home-Verzeichnis im Folder neo4j/data angelegt (bleibt bestehen). 
   Um diese zu löschen: 
   
        > sudo rm -r /home/pkmlp/neo4j/data 

   Um die (gestoppten) Container und die Images wegzuräumen:

        > /home/pkmlp/myTools/dockerCleanup
