import os
from pytube import YouTube
print("Inciando convertidor.. \n")
file = open('lista.txt', 'r')
print("cargando lista de canciones a descargar... \n\n")
i=0
for item in file:
    yt=YouTube(item)
    nombre = yt.title
    i+=1
    print("video: ",nombre," url: ",item)
    cancion = yt.streams.filter(only_audio=True).first()
    salida = cancion.download(output_path="./")
    base, ext = os.path.splitext(salida)
    nuevo = base + '.mp3'
    os.rename(salida,nuevo)
    print("Cancion descargada \n")
print("Descargas completadas ", i, " :", " ",i)