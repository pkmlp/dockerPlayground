
In diesem Beispiel erstellen wir (wieder - siehe unbedingt auch myFirstDbApp) einen Container mit einem MySQL Datenbank Server. Der Container selbst enthält wiederum kein GUI für die Datenbank, nur den Datenbank-Server mit dem Command-Line-Client für den Zugriff auf die Datenbank. Der Container soll als "DB as a Service" laufen. Auch für dieses zweite Beispiel nehmen wir das im Docker-Repository angebotene offizielle MySQL-Image, ABER ... 

... in diesem Beispiel wollen wir:

1. Die Daten der DB auf dem Docker-Host haben und
2. Ein Verzeichnis auf dem Docker Host mit dem Container teilen, über das z.B. SQL-Scripts "ausgetauscht" werden können

Das heisst, dass wir dem Container die beiden Verzeichnisse mounten müssen. Wie im Beispiel mit der PythonFlaskApp gesehen, erfolgt dies mit dem Parameter -v beim Start des Containers.



==========
Version 1: 
==========

Auch in dieser Version wollen wir nur mittels SQL-Command-Line-Client (im Container) auf die Datenbank zugreifen.


Einen MySQL Container mit dem offiziellen Image vom Docker Repository starten wir mit:

    > docker run -d --name mySecondDbApp  \
                 -e MYSQL_ROOT_PASSWORD=pkmlp \
                 -v /home/pkmlp/dockerWork/MySqlApps/mySecondApp/mySqlData:/var/lib/mysql   \
                 -v /home/pkmlp/dockerWork/MySqlApps/mySecondApp/mySqlShare:/usr/src/mysql   \
                 mysql:5.7

Hinweise:

 - Der Container wird im im detached Mode (-d) gestartet
 - Der Container erhält den Namen mySecondDbApp (Container können Gross- und Kleinbuchstaben enthalten)
 - Im Container wird das Root-Passwort für MySQL (pkmlp) gesetzt 
 - Dem Container wird das Verzeichnis das die Daten der DB enthalten soll zugewiesen
 - Dem Container wird das Verzeichnis das als Tauschbörse fungieren soll zugewiesen
 - Für den Container wird das Image mit Namen mysql in Version 5.7 genommen (MySQL 5.7). Da wir kein eigenes Image erzeugt haben, wird dieses ab dem Docker-Hub geholt.



Auf den Container kann zugegriffen werden mit:

    > docker exec -it mySecondDbApp bash                   (eröffnet eine Bash-Shell, aus der dann der MySQL-Client mit "mysql -u root -p" aufgerufen werden kann)            
    > docker exec -it mySecondDbApp mysql -u root -p       (eröffnet eine Session direkt im MySQL Client)



Wichtige Hinweise:

1) Der Container ist nun nicht mehr komplett isoliert. Alle Daten sind in einem Verzeichnis auf dem Docker-Host. Wird der Container gelöscht (kill, rm), so sind die Daten nicht verloren. Zusätzlich haben wir sogar ein Verzeichnis auf dem Docker Host eingerichtet, über das SQL-Scripts oder anderes ausgetaucht werden können. So könnte z.B. auch ein DB-Backup gemacht werden und dieser im geteilten Verzeichnis abgelegt werden. 

2) Beide Verzeichnisse sind nun sowohl intern im Container wie auch von extern im Docker-Host zugreifbar.



==========
Version 2: 
==========

In dieser Version greifen wir auch mit einem SQL-GUI-Client auf dem Docker-HOST auf die DB im Container zu.


Einen MySQL Container mit dem offiziellen Image vom Docker Repository starten wir mit:

    > docker run -d --name mySecondDbApp  \
                 -e MYSQL_ROOT_PASSWORD=pkmlp \
                 -v /home/pkmlp/dockerWork/MySqlApps/mySecondApp/mySqlData:/var/lib/mysql   \
                 -v /home/pkmlp/dockerWork/MySqlApps/mySecondApp/mySqlShare:/usr/src/mysql   \
                 -p 3306:3306 \
                 mysql:5.7

Hinweise:

 - Der Container wird im im detached Mode (-d) gestartet
 - Der Container erhält den Namen mySecondDbApp (Container können Gross- und Kleinbuchstaben enthalten)
 - Im Container wird das Root-Passwort für MySQL (pkmlp) gesetzt 
 - Dem Container wird das Verzeichnis das die Daten der DB enthalten soll zugewiesen (ist vor dem erstmaligen Starten des Containers leer)
 - Dem Container wird das Verzeichnis das als Tauschbörse fungieren soll zugewiesen (enthält ein Script zum Testen)
 - Wir mappen den Port 3306 im Container auf den Port 3306 im Docker Host
 - Für den Container wird das Image mit Namen mysql in Version 5.7 genommen (MySQL 5.7). Da wir kein eigenes Image erzeugt haben, wird dieses ab dem Docker-Hub geholt.



Auf den Container kann (nach wie vor) zugegriffen werden mit:

    > docker exec -it mySecondDbApp bash                   (eröffnet eine Bash-Shell, aus der dann der MySQL-Client mit "mysql -u root -p" aufgerufen werden kann)            
    > docker exec -it mySecondDbApp mysql -u root -p       (eröffnet eine Session direkt im MySQL Client)



Zusätzlich können wir nun aber mit dem SQL-GUI-Client im Docker Host eine Verbindung über den Port 3306 in den Container aufbauen. Im dockerPlayground ist der SQL-GUI-Client Sqlectron installiert. Versuchen wir es damit.



Wichtige Hinweise:

1) Der Container ist nun nicht mehr komplett isoliert. Alle Daten sind in einem Verzeichnis auf dem Docker-Host. Wird der Container gelöscht (kill, rm), so sind die Daten nicht verloren. Zusätzlich haben wir sogar ein Verzeichnis auf dem Docker Host eingerichtet, über das SQL-Scripts oder anderes ausgetaucht werden können. So könnte z.B. auch ein DB-Backup gemacht werden und dieser im geteilten Verzeichnis abgelegt werden. 

2) Beide Verzeichnisse sind nun sowohl intern im Container wie auch von extern im Docker-Host zugreifbar.



