# Set base image
FROM python:3-slim

# Create root directory for project
RUN mkdir /home/naturalSelectionSimulator

# Create directory for grid
RUN mkdir /home/naturalSelectionSimulator/grid

# Create directory for ecosystem
RUN mkdir /home/naturalSelectionSimulator/ecosystem

# Create directory for ecosystem
RUN mkdir /home/naturalSelectionSimulator/logging

# Set workdir
WORKDIR /home/naturalSelectionSimulator

# Copy config files
COPY ./gridConfig.json /home/naturalSelectionSimulator
COPY ./defaultPlayerConfig.json /home/naturalSelectionSimulator

# Copy index file
COPY ./index.py /home/naturalSelectionSimulator

# Copy player code
COPY ./player.py /home/naturalSelectionSimulator

# Copy search code
COPY ./search.py /home/naturalSelectionSimulator

# Copy grid code
COPY ./grid/* /home/naturalSelectionSimulator/grid/

# Copy grid code
COPY ./ecosystem/* /home/naturalSelectionSimulator/ecosystem/

# Copy readme file
COPY ./README.md /home/naturalSelectionSimulator
COPY ./requirements.txt /home/naturalSelectionSimulator

# Install python modules
RUN pip install -r requirements.txt

# Expose volume
VOLUME /logging

# Set entrypoint
ENTRYPOINT ["python", "index.py"]
