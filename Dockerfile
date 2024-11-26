# Use the official Python image as the base image
FROM python:3.8
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

# Set the working directory in the container
WORKDIR /app
# Copy the application files into the working directory
COPY . /app

COPY ./requirements.txt /var/www/requirements.txt
# Install the application dependencies
RUN pip install -r /var/www/requirements.txt

# Define the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0"]
