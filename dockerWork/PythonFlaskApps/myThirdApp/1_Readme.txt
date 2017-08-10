
In diesem (dritten) Beispiel erstellen wir (wiederum) einen Container, der eine Python-Flask-Anwendung (diesmal eine etwas aufwändigere App) enthält (beachte dazu unbedingt die Readme-Datei im ersten Beispiel: myFirstApp). 

Der Unterschied zum ersten Beispiel ist der, dass die Programm-Sourcen nicht beim erstellen des Images in dieses kopiert werden, sondern dass diese zur Laufzeit dem Container ab dem Filesystem des Docker-Hosts zugänglich gemacht werden.

Dazu müssen folgende Komponenten angepasst werden:

1) Im Dockerfile werden die Programm Sourcen nicht mehr in das Image kopiert. Die Copy-Befehle für die Programm-Sourcen werden einfach gelöscht.
2) Beim Starten des Containers muss der Ordner mit den Programm-Sourcen in den Container gemappt werden (zugänglich geamcht werden).
 


Das Image wird erstellt mit:

    > docker build -t mythirdapp .

Hinweise:
 - Images können nur mit Kleinbuchstaben benannt werden
 - Damit dieser Docker-Befehl funktioniert, müssen wir im Terminal in diesem Ordner positioniert sein
 - Der Punkt am Ende des Docker-Befehls ist wichtig, weil damit der Ort des Dockerfiles bekannt gegeben wird



Ist das Image erstellt, kann der Container gestartet werden mit:

    > docker run -d -p 8080:5000 --name myThirdApp -v /home/pkmlp/gitRepos/dockerPlayground/dockerWork/PythonFlaskApps/myThirdApp:/usr/src/app/ mythirdapp

Hinweise:

 - Der Container wird detached (als Daemon) gestartet
 - Der im Container nach aussen freigegebene Port 5000 wird auf den Port 8080 im Docker Host gemappt 
 - Der Container wird gestartet mit dem Namen myThirdApp (Container könne Gross- und Kleinbuchstaben enthalten)
 - Der Ordner mit den Programm Sourcen (der aktuelle Ordner) auf dem Docker-Host wird in das entsprechende Verzeichnis im Container gemappt
 - Für den Container wird das Image mit Namen mythirdapp genommen

Die App (siehe Source-Code HelloFlask.py) muss mit Parameter host="0.0.0.0" gestartet werden. Dies da der Flask-Web-Server per Default nur Verbindungen ab Localhost annimmt. Da der Container jedoch eine isolierte Einheit ist und wir mit dem Browser von ausserhalb zugreifen wollen, muss die App mit diesem Parameter gestartet werden.

