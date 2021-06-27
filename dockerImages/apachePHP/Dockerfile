FROM centos:7

RUN \
  yum -y install \
  httpd \
  php \
  php-cli \
  php-common \
  mod_ssl \
  openssl

#COPY ssl.conf /etc/httpd/conf.d/default.conf

#COPY docker.crt /docker.crt

#COPY docker.key /docker.key

COPY web /var/www/html

RUN useradd apachephp

RUN chown apachephp:apachephp /var/www/html -R


LABEL version:v6 \
      descripcion: centos7 php para montor app \
      vendor:AngelHdez

# usuario creado para manejar sitio
USER apachephp

RUN echo "<?php phpinfo(); ?>" > /var/www/html/hola.php

USER root

RUN chmod 777 /var/www/ -R

EXPOSE 80

CMD apachectl -DFOREGROUND
