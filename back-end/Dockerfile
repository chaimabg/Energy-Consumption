# pull official base image
FROM python:3.10-alpine

# Create app directory
WORKDIR /app

# set environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install gcc and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Install app dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

#Container listening port
EXPOSE 5000

# Run the application when the container launches
CMD ["flask", "run"]