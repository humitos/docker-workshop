Local NGINX server
------------------

This server is to easily provide the Docker installers for Mac and
Windows and also all the Docker images saved by `docker save` to be
used with `docker load` in case the Docker Registry under the local
network is not an option.

Copy all your files under `./data` folder and run::


  docker-compose up

Then, communicate your local IP to the rest of the class so they can
access to your files easily.
