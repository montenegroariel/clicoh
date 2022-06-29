<<<<<<< HEAD
# Clicoh Ecommerce

Crear una API REST utilizando DJANGO REST FRAMEWORK, que brinde la funcionalidad básica y acotada de un
Ecommerce.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

git clone https://github.com/montenegroariel/clicoh.git

cd clicoh

sudo docker-compose up

En la consola
```
sudo docker ps

CONTAINER ID   IMAGE                  COMMAND                  CREATED        STATUS       PORTS                                           NAMES
0b1b376975c8   clicoh_web             "/usr/src/app/entryp…"   30 hours ago   Up 6 hours   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp       clicoh_web_1
3be840a4d20c   postgres:12.0-alpine   "docker-entrypoint.s…"   30 hours ago   Up 6 hours   5432/tcp                                        clicoh_db_1

```

copiar el id del contenedor clicoh_web


docker exec -it <id_container> python manage.py migrate

docker exec -it <id_container> python manage.py createsuperuser

ingresar user y password

### Pre-requisitos 📋

_software y como instalarlas_

git

https://git-scm.com/downloads

docker

https://www.docker.com/get-started

docker-compose

https://docs.docker.com/compose/install/


### Instalación Ubuntu 20.04 🔧

```
sudo apt update
sudo apt-get install git docker docker-compose
```

## Ejecutando las pruebas ⚙️

El usuario una vez que se encuentra logeado puede dar de alta los productos con el valor y stock deseado. A partir de ese momento se generan las ordenes que contaran con sus respectivos detalles para realizar las consultas o modificaciones necesarias.
El valor de la orden en dolares se consulta del sitio https://www.dolarsi.com/api/api.php?type=valoresprincipales

Se puede importar en postman de manera local el archivo
clicoh.postman_local.json

## Test ⚙️

Correr el proyecto con docker-compose up

En la consola
```
sudo docker ps

CONTAINER ID   IMAGE                  COMMAND                  CREATED        STATUS       PORTS                                           NAMES
0b1b376975c8   clicoh_web             "/usr/src/app/entryp…"   30 hours ago   Up 6 hours   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp       clicoh_web_1
3be840a4d20c   postgres:12.0-alpine   "docker-entrypoint.s…"   30 hours ago   Up 6 hours   5432/tcp                                        clicoh_db_1
```

copiar el id del contenedor clicoh_web

docker exec -it <id_container> python manage.py test


Ejemplo:

```
docker exec -it 0b1b376975c8 python manage.py test
```


## Endpoints ⚙️

Login

(http://localhost:8000/login/)

Listar ordenes

(http://localhost:8000/orders/)

Listar productos

(http://localhost:8000/products)


## Despliegue 📦

El proyecto se encuentra corriendo en https://clicoh.seostax.com

Para realizar pruebas en producción se puede importar el archivo 
clicoh.postman_production.json

## Construido con 🛠️


* [Django](https://www.djangoproject.com/) - El framework web usado
* [Django Rest Framework](https://www.django-rest-framework.org/) - API Rest
* [Docker](https://www.docker.com/) - Containers
* [Postgresql](https://www.postgresql.org/) - Base de datos



## Expresiones de Gratitud 🎁

* Gracias por el template [Villanuevand](https://github.com/Villanuevand)
---

=======
# clicoh
>>>>>>> 2d1b723 (first commit)
