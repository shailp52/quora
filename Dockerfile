# Base Image as django image is deprecated
FROM python:2.7.18-buster
# python environment
ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONUNBUFFERED 1 # Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1
# expose port
EXPOSE 8000
# switch to working directory
WORKDIR /usr/src/Trainman
# install os packages
RUN apt-get update && apt-get -y install gcc mono-mcs
# update repositories and install netcat and clean the tempemporary directories
RUN apt-get install -y default-libmysqlclient-dev build-essential
# for scipy==1.1.0
RUN apt-get -y install gfortran liblapack-dev libblas-dev
# Copy the project files and run the CMD
COPY . .
# install dependencies
RUN pip install -r requirements.txt

# Create log file on src directory
# RUN mkdir -p /usr/src/logs && touch /usr/src/logs/access.log && chmod -R  777 /usr/src/logs/access.log

# # Create log file on home directory
# RUN mkdir -p /home/logs && touch /home/logs/access.log && chmod -R  777 /home/logs/access.log

# RUN python update_train_js.py
# python django run server.
# CMD ["tail", "-f", "/dev/null"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]