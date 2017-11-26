Run these commands from this folder.

Script for Python 2.7:

.. code:: bash

   docker run \
     --rm \
     -v `pwd`/script27.py:/usr/source/app/script27.py \
     -w /usr/source/app \
     python:2.7 \
     python script27.py

Script for Python 3.6:

.. code:: bash

   docker run \
     --rm \
     -v `pwd`/script36.py:/usr/source/app/script36.py \
     -w /usr/source/app \
     python:3.6 \
     python script36.py
