# Use an existing jupyter/datascience-notebook image as a base
FROM jupyter/datascience-notebook:2023-05-30

# Run as root to install software
USER root

# Install HTTrack
RUN apt-get update && \
    apt-get install -y httrack && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch back to the non-root user
USER jovyan