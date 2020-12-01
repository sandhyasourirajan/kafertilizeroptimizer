# Create image based in the official nginx - Alpine image

FROM nginx:1.13.7-alpine
RUN rm -rf /usr/share/nginx/html
COPY dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
