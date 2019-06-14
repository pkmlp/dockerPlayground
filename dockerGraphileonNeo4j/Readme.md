
# Graphileon and Neo4j in Docker Containers

The docker-compose configuration allows you to setup graphileon with one application database (host=neo4j-graphileon, user=neo4j, password=graphileon) and one playground database (host=neo4j-playground, user=neo4j, password=playground).

The script allows you to load the graphileon docker image into your local repository so that a `Dockerfile`/`docker-compose.yml` can reference it as `graphileon:latest`load.sh 
