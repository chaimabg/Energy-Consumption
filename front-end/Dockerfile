FROM node:16
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . .
ENV PORT=8080
EXPOSE ${PORT}
CMD npm start



