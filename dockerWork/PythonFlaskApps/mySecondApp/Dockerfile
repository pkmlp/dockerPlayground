
# Definieren des Base-Images, auf dem wir aufsetzen wollen
FROM alpine:edge

# Installieren von Python im Base-Image
RUN apk add --update py2-pip

# Installation der Python-Module, die von der Python-Anwendung benötigt werden
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Flask arbeitet mit Port 5000. Wir müssend diesen Port nach aussen freigeben
EXPOSE 5000

# Starten der Python-Flask Anwendung
CMD ["python", "/usr/src/app/app.py"]

