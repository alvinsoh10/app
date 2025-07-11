FROM nginx:alpine
# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom Nginx configuration file into the container
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

COPY helloworld.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]