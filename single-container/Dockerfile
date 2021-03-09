# A test web app, returns name of host/pod/container servicing request
# Linux x64
FROM node:current-alpine

LABEL org.opencontainers.image.title="Helo Docker Learners!" \
        org.opencontainers.image.description="Web server showing host that responds" \
        org.opencontainers.image.authors="@nigelpoulton"

# Create directory in container image for app code
RUN mkdir -p /usr/src/app

# Copy app code from current dir into container image
COPY . /usr/src/app

WORKDIR /usr/src/app

# Install dependencies from package.json
RUN npm install

# Command for container to execute
ENTRYPOINT [ "node", "app.js" ]