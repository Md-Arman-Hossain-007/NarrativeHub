FROM nginx:1.23.3-alpine

# remove the default configuration of nginx
RUN rm /etc/nginx/conf.d/default.conf

# copy the customize nginx default configuration
COPY ./default.conf  /etc/nginx/conf.d/default.conf