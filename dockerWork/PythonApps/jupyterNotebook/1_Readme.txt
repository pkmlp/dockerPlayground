
In diesem Beispiel erstellen wir einen Container, der Python mit dem Jupyter Notebook enthält. Wir verwenden dafür das "vorhandene" Image jupyter/scipy-notebook und starten den Container mit:

    > docker run      \
             -d       \
             --rm     \
             -p 8888:8888   \
             -v /home/pkmlp/gitRepos/dockerPlayground/dockerWork/PythonApps/jupyterNotebook/Notebooks:/home/jovyan/work    \
             --name pythonJupyter    \
             jupyter/scipy-notebook start-notebook.sh --NotebookApp.token=''  

Hinweise:

 - Der Container wird detached (als Daemon) gestartet
 - Der im Container nach aussen freigegebene Port 8888 wird auf den Port 8888 im Docker Host gemappt 
 - Dem Container wird ein Verszichnis auf dem Docker-HOST mit den Notebooks zugewiesen (/home/jovan/worl ist von der Distro gegeben)
 - Der Container wird gestartet mit dem Namen pythonJupyter (Container können Gross- und Kleinbuchstaben enthalten)
 - Für den Container wird das offizielle Image mit Namen ipython/scipyserver genommen


Das JupiterNotebook kann dann mit dem Browser wie folgt aufgerufen werden:

    > firefox localhost:8888



Hinweis: Das Verzeichnis Notebooks das sich im gleichen Verzeichnis wie dieses Readme befindet, hat es ein Beispiel Notebook. 


