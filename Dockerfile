FROM nginx:alpine
COPY helloworld.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]