
In diesem Beispiel erstellen wir einen Container, der eine Python-Flask-Anwendung enthält, die ein zufällig ausgewähltes Katzenbild zeigt.

Mit Python und Flask können Web-Anwendungen erstellt werden. Die Anwendung gibt lediglich eine statische Web-Seite zurück, die ein aus einer Liste im Programm ausgewähltes Katzenbild zeigt. Bei jedem Refresh der Seite wird ein anderes Bild aus der Liste ausgewählt. Der Container ist komplett isoliert. Beachte dazu unbedingt das Dockerfile. 



Das Image wird erstellt mit:

    > docker build -t myfirstapp .

Hinweise:
 - Images können nur mit Kleinbuchstaben benannt werden
 - Damit dieser Docker-Befehl funktioniert, müssen wir im Terminal in diesem Ordner positioniert sein
 - Der Punkt am Ende des Docker-Befehls ist wichtig, weil damit der Ort des Dockerfiles bekannt gegeben wird



Ist das Image erstellt, kann der Container gestartet werden mit:

    > docker run -d -p 8888:5000 --name myFirstApp myfirstapp

Hinweise:

 - Der Container wird detached (als Daemon) gestartet
 - Der im Container nach aussen freigegebene Port 5000 wird auf den Port 8000 im Docker Host gemappt 
 - Der Container wird gestartet mit dem Namen myFirstApp (Container könne Gross- und Kleinbuchstaben enthalten)
 - Für den Container wird das Image mit Namen myfirstapp genommen

Die App (siehe Source-Code app.py) muss mit Parameter host="0.0.0.0" gestartet werden. Dies da der Flask-Web-Server per Default nur Verbindungen ab Localhost annimmt. Da der Container jedoch eine isolierte Einheit ist und wir mit dem Browser von ausserhalb zugreifen wollen, muss die App mit diesem Parameter gestartet werden.




