Setup a Local Network Docker Registry
-------------------------------------

1. Add an `A` in you DNS: https://www.cloudflare.com/a/dns/argentinaenpython.com
1. Open the 443 port in your router to be accessible from outside
   * I activated DMZ
1. Run `certbot` to create your HTTPS certificate

.. code:: bash

   pacman -S certbot
   sudo certbot certonly

1. Copy the certificates in your home directory

.. code:: bash

   make ~/.ssl/registry
   sudo su -c 'cp /etc/letsencrypt/live/docker.argentinaenpython.com/* ~/.ssl/registry/

1. Run the registry container:

.. code:: bash
   
   docker-compose up -d

1. Update the registry in the the DNS to point to your local network IP


References
----------

* https://github.com/docker-oxford/local-registry
* https://docs.docker.com/registry/deploying/
