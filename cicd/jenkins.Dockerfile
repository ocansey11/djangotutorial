# Start from the official Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to root user to install Python
USER root

# Update and install Python + pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python

# Switch back to Jenkins user
USER jenkins
