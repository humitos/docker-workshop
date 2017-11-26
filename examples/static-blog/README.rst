Run this command on this folder:

.. code:: bash

   docker run \ 
     --rm \
     -p 8000:80 \
     -v .:/usr/share/nginx/html:ro \
     nginx


Custom example with the Argentina en Python full website content:

.. code:: bash

   docker run \
     -p 8000:80 \
     -v `pwd`/html:/usr/share/nginx/html:ro \
     -v `pwd`/nginx.docker.conf:/etc/nginx/nginx.conf:ro \
     nginx


Add the website content inside the image.

Build the image with the content:

.. code:: bash

   docker build -t mysite .


Run the image:

.. code:: bash

   docker run -p 8000:80 mysite

   
