FROM ubuntu:16.04

# um Probleme mit Dialog-Wizards zu vermeiden
ENV DEBIAN_FRONTEND noninteractive 

# Installation der MySQL-Workbench 
RUN apt-get update && apt-get install -y mysql-workbench 

# starten der MySQL-Workbench
CMD mysql-workbench
