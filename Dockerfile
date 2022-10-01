# start by pulling a base image.
FROM ubuntu
# update the repositories.
RUN apt-get update && apt-get -y upgrade
# Install apt utilities.
RUN apt install apt-utils
# Add the environment variable.
ENV BACK_GROUND E80F88
# Install Python and PIP.
RUN apt install -y python3 && apt install -y pip
# Install Flask Package for the execution of Flask Application.
RUN pip install Flask
# Install Git, as we will use it for cloning the source code.
RUN apt install -y git
# Clone the Git repository for the source code.
RUN git clone https://github.com/NarendraGodi/docker_env_flask.git
# switch working directory
WORKDIR /docker_env_flask
# Execute the application.
ENTRYPOINT FLASK_APP=/docker_env_flask/app.py flask run --host=0.0.0.0 --port=8080
# make sure the container doesnt exit.
CMD tail -f /dev/null