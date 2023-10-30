FROM node:16-alpine3.17 as build-stage

# Set the working directory
WORKDIR /app

# Copy the working directory in the container
COPY package*.json ./

# install the project dependencies
RUN npm install

# copy the rest of the project files to the container
COPY . .

# build the vue.js application to the production mode to dist folder
RUN npm run build

# use the lightweght Nginx image from the previous state to the nginx container
FROM nginx:stable-alpine as production-stage

# copy the build application from the previous state to the nginx container
COPY --from=build-stage /app/dist /usr/share/nginx/html

COPY nginx/nginx.conf /etc/nginx/nginx.conf

# expose the port 80
EXPOSE 80

# start nginx to server app
CMD ["nginx", "-g", "daemon off;"]
