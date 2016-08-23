Instale virtualenv para manejar entornos virtuales independientes y no afectar los paquetes de python del sistema

`$ sudo apt-get install python-virtualenv`

cree el entorno virtual 

```
$ mkdir ~/entornos
$ virtualenv -p python3 ~/entornos/buses
```

Posicionese en el entorno virtual y actualice pip

```
$ source ~/entornos/buses/bin/activate
($) pip install --upgrade pip setuptools
```

Instale pyexcel

```
($) pip install pyexcel
($) pip install pyexcel-xls
```

Para correr el programa 

`($) python extrae_rutas_y_empresas.py`

Dentro del código hay explicación de como hacer la limpieza de datos.

**Nota:*** Se podría usar pandas para hacer análisis apartir de la información recopilada
