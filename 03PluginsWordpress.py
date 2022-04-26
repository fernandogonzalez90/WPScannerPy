# Encontrnado plugins con fuerza bruta
import requests
from os import path
from progress.bar import Bar

if path.exists('wp_plugins.txt'):
    archivo = open('wp_plugins.txt', 'r')
    archivo = archivo.read().split('\n')
    lista = []
    url = 'https://gonzalezelectricista.com.ar'
    bar = Bar('Espere...', max=len(archivo))

    for plugin in archivo:
        bar.next()
        try:
            peticion = requests.get(url=url + '/' + plugin)
            if peticion.status_code == 200:
                final = url + '/' + plugin
                lista.append(final.split('/')[-1])
        except:
            pass
    bar.finish()

    for plugin in lista:
        print(f'Plugin encontrado: {plugin}')
else:
    print('No existe el archivo.')
