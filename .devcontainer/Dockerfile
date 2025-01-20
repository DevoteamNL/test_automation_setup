# Use the official Ubuntu Noble base image
FROM ubuntu:noble

# Set environment variables for non-interactive apt and prevent cache bloating
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# Update packages, install dependencies, and set up Node.js (v22)
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        wget \
        git \
        sudo \
        openssh-client \
        ca-certificates \
        tzdata && \
    # Install Node.js v22 (using Nodesource)
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    # Verify Node.js and npm installations
    node -v && npm -v && \
    # Clean up package cache to reduce image size
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Playwright globally along with its dependencies
RUN npm install -g playwright

# Create a non-root user with sudo privileges
ARG USERNAME=ubuntu

RUN echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# Switch to the non-root user
USER $USERNAME

# Set the working directory
WORKDIR /home/$USERNAME

# Install Playwright system dependencies
RUN npx playwright install-deps && \
    # Install Playwright browsers
    npx playwright install && \
    # Verify Playwright installation
    npx playwright --version

# Default shell for the user
SHELL ["/bin/bash", "-c"]

# Default command
CMD ["bash"]
