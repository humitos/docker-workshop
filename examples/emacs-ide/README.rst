Run this command from this folder:

.. code:: bash

   docker run \
     --rm \
     -e DISPLAY \
     -v $(pwd):/src \
     -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
     -v $XAUTHORITY:/root/.Xauthority \
     --net=host \
     humitos/emacs-x11-alpine


* https://hub.docker.com/r/humitos/emacs-x11-alpine/
* https://github.com/humitos/emacs-x11-alpine/
