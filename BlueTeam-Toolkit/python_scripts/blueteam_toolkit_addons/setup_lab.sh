#!/bin/bash

# Install packages
sudo apt update
sudo apt install -y nginx python3-pip tshark

# Install Python dependencies
pip install geoip2

# Start NGINX
sudo systemctl start nginx

# Setup complete
