Run this command from this folder:

.. code:: bash

   docker run \
     --hostname gitlab.example.com \
     --publish 8000:80 \
     --name gitlab \
     --volume /tmp/gitlab/config:/etc/gitlab \
     --volume /tmp/gitlab/logs:/var/log/gitlab \
     --volume /tmp/gitlab/data:/var/opt/gitlab \
     gitlab/gitlab-ce:latest
