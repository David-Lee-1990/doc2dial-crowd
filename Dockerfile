# Start with a python 3.5 image
FROM python:3

# Document who is responsible for this image
MAINTAINER Kshitij Fadnis "kpfadnis@us.ibm.com"

# Expose any ports the app is expecting in the environment
ENV PORT 8081
EXPOSE $PORT

# Expose domain the app is expecting in the environment
ENV domain it

# Set up a working folder and install the pre-reqs
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt

# Add the code as the last Docker layer because it changes the most
ADD webapp /app/webapp
ADD configs /app/configs
ADD run.py /app

# Run the service
CMD [ "python", "run.py" ]
