
In diesem Beispiel erstellen wir einen Container mit einem MySQL Datenbank Server. Der Container selbst enthält kein GUI für die Datenbank, nur den Datenbank-Server mit dem Command-Line-Client für den Zugriff auf die Datenbank. Der Container soll als "DB as a Service" laufen. Für dieses erste Beispiel nehmen wir das im Docker-Repository angebotene offizielle MySQL-Image.
 

==========
Version 1: 
==========

In dieser Version wollen wir nur mittels SQL-Command-Line-Client (im Container) auf die Datenbank zugreifen.


Einen MySQL Container mit dem offiziellen Image vom Docker Repository starten wir mit:

    > docker run --name myFirstDbApp -e MYSQL_ROOT_PASSWORD=pkmlp -d mysql:5.7

Hinweise:

 - Der Container wird gestartet mit dem Namen myFirstDbApp (Container können Gross- und Kleinbuchstaben enthalten)
 - Im Container wird das Root-Passwort für MySQL (pkmlp) gesetzt 
 - Der Container wird im im detached Mode (-d) gestartet
 - Für den Container wird das Image mit Namen mysql in Version 5.7 genommen (MySQL 5.7)



Auf den Container kann zugegriffen werden mit:

    > docker exec -it myFirstDbApp bash                   (eröffnet eine Bash-Shell, aus der dann der MySQL-Client mit "mysql -u root -p" aufgerufen werden kann)            
    > docker exec -it myFirstDbApp mysql -u root -p       (eröffnet eine Session direkt im MySQL Client)



Wichtiger Hinweis:

1) Der Container ist komplett isoliert. Alle Daten sind im Container. Wird der Container gelöscht (kill, rm), so sind die Daten verloren. Wird der Container einfach gestoppt und dann wieder gestartet, so sind die Daten im Container vorhanden. 





==========
Version 2: 
==========

In dieser Version greifen wir auch mit einem SQL-GUI-Client auf dem Docker-HOST auf die DB im Container zu.


Einen MySQL Container mit dem offiziellen Image vom Docker Repository starten wir mit:

    > docker run --name myFirstDbApp -e MYSQL_ROOT_PASSWORD=pkmlp -d  -p 3306:3306 mysql:5.7

Hinweise:

 - Der Container wird gestartet mit dem Namen myFirstDbApp (Container können Gross- und Kleinbuchstaben enthalten)
 - Im Container wird das Root-Passwort für MySQL (pkmlp) gesetzt 
 - Der Container wird im im detached Mode (-d) gestartet
 - Wir mappen den Port 3306 im Container auf den Port 3306 im Docker Host
 - Für den Container wird das Image mit Namen mysql in Version 5.7 genommen (MySQL 5.7)



Auf den Container kann (nach wie vor) zugegriffen werden mit:

    > docker exec -it myFirstDbApp bash                   (eröffnet eine Bash-Shell, aus der dann der MySQL-Client mit "mysql -u root -p" aufgerufen werden kann)            
    > docker exec -it myFirstDbApp mysql -u root -p       (eröffnet eine Session direkt im MySQL Client)



Zusätzlich können wir nun aber mit dem SQL-GUI-Client im Docker Host eine Verbindung über den Port 3306 in den Container aufbauen. Im dockerPlayground ist der SQL-GUI-Client Sqlectron installiert. Versuchen wir es damit.



Wichtiger Hinweis:

1) Der Container ist immer noch komplett isoliert. Alle Daten sind im Container. Wird der Container gelöscht (kill, rm), so sind die Daten verloren. Wird der Container einfach gestoppt und dann wieder gestartet, so sind die Daten im Container vorhanden. 




