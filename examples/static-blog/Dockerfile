FROM nginx:latest

# Docker doesn't support this `./html` being a symlink
COPY ./html /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf
